# AlleyGator

A bowling scoreboard as a takeaway challenge for an SDET position with Experis'
gaming branch.

## Reflections

* I started with a lot of flailing around.
  * How do I create a "production-ready" graphical app in Python?
  * How do I write unit tests in Python?
  * How can I get Sekili working to get familiar with the application?
  * What do I build first, the UI or the logic?
* I need to slow down and prioritize.
  * The application has two parts: the GUI and the logic.
    * I need to design a model for the application logic based on the example.
      * I need a language I can use to describe the objects involved.
        * There are Frames, which have three things: a number, a tuple of pin
          counts, and a final score for that frame.
          * There is a special Frame, the FinalFrame if you will, which has three
            pin counts instead of the two that the other Frames have.
          * Frames need to know about the next Frame (except for the FinalFrame)
            * If a Frame contains a strike, it needs to look ahead to the next
              Frame and add the value of the next two shots.
              * If the next shot is a strike, then you need to skip to the _next_
                Frame.
              * What happens when the player makes all strikes?
            * If a Frame contains a spare, it needs to look ahead to the next
              Frame and add the value of the next shot.
              * No need to look further than the next Frame.
          * Frames also need to know about the previous Frame, as a Frame's
            score is the sum of its current pin counts and the score of the
            previous frame.
          * Smells like ~~teen spir-~~ a doubly-linked list.
            * Thank god it's not circular.
        * What do I call a list of Frames?
          * A ScoreCard?
          * A Row?
            * Assumes a more tabular format, as you'd expect for keeping track
              of multiple players.
    * I need to design a UI based on the example.
      * I need a Renderer to map the logic to the UI.
        * But I also need to give the logic access to the inputs.
          * Tk uses global variables to store state.
            * For our use case, we need _three_ pieces of state for each
              Frame and _four_ for the FinalFrame.
            * These pieces of state are the pin counts for shots one, two, and
              three, as well as the score for that Frame.
            * Not only does each Frame need to monitor its state, but it
              also needs to monitor the state changes of the Frames it depends
              on.
          * The best way I can think to tackle this is to store these pieces of
            state in the Frames themselves, then tie the UI to the Frames at
            startup:
            1. Create an instance of the ScoreCard, which initializes all the
              Frames.
            2. Pass the ScoreCard to the UI setup, which will tie the relevant
              UI elements to the state stored in each Frame.
* Thoughts as I implement
  * While the idea to have state stored in the Frames sounded like a good idea,
    it seems like that was naive.
    * Issues:
      1. Tkinter widget variables require a Tk instance to be created before you
        use them, otherwise, they will crash due to not having a master frame.
      2. Tkinter widget variables do not behave like their native counterparts.
        * You can't use an IntVar like an int, a StringVar like a string, etc...
    * A better idea: decouple UI from data using subscriber pattern.
      * Data class posts change events whenever a value is modified.
      * UI class subscribes to data class change events.
    * OK, tried the "better idea" and my initial implementation came with a
      severe gotcha:
      * `__setattr__` overrides all assignments to an object, including those in
        the constructor!
        * WHY!?!?
      * This means that monkey-patching assignments like we are used to in
        JavaScript or C# does not work and we need a new way to subscribe to
        value changes rather than listening in on attribute value assignments.
        * Makes me think of using the idea of atoms instead, where the values
          themselves are subscribable.
        * Simpler, more immediate implementation: just use functions to set the
          value instead.
    * Additional gotcha I'm having difficulty navigating: for some reason when
      I assign a value to the attribute of a class instance, it affects other
      instances???
      * I'm missing something, and there's a sense I'm getting from
        documentation snippets I've read that it has something to do with
        inheritance from `object`.
        * What is the "new style" I've been reading about with objects???
        * Removing the inheritance from `object` did nothing to change the tests.
          * Figured it out: default arguments are passed by reference.
            * WHY!?!?
            * Turns out that when you declare a mutable object as the default
              value for an argument, it belongs to a higher scope and is passed
              by reference to each function call.
              * This could be used to maintain function-local state that persists
                between calls ala C static variables inside functions.
  * As I iterate on implementing a subscriber/observer pattern for mapping
    changes back and forth, a different method is forming in my head
    * What if we stored all state in a single data object, forgoing the whole
      linked list idea and Frames that autonomously update themselves?
    * It'd be a hack, but it could work, and we'd be able to move faster than
      worrying about relatively minute architecture concerns.
    * Scrapping this idea because it's a hack, but not a _testable_ hack.
  * Something I didn't originally anticipate but see now with the Frames is that
    the data transmission is two-way:
    * Data enters the Frames from Tkinter via the inputs.
    * Data leaves the Frames via the computed score.
    * We have a cycle of data:
      1. The user updates a point entry in a frame in the UI.
      2. Tkinter notifies the concerned Frame (who is subscribed to Tkinter)
        that the point entry has changed, and provides it the new value in via
        a registered callback.
      3. The Frame's callback invokes a "compute score" function, then notifies
        Tkinter that the score has changed.
         * The Frame also notifies "upstream" Frames that the score has updated,
           triggering their "compute scores," which also notify Tkinter.
      4. Tkinter updates the scores as they come in, eventually landing back at
        a steady state waiting for user input.
         * Will we want to have a queue to make sure that inputs are handled in
           the order they are completed?
           * I only consider this because of JavaScript's async logic and a desire
             to avoid a race condition.
  * Pivoting hard to a more productive angle.
    * Instead of getting stuck into the weeds about the logic and backend, I'm
      pivoting to building the UI and figuring out how to, as simply as possible,
      manage the state of the application.
    * As I pivot, I'm looking solely at the UI and stripping down everything to
      as bare as I can get.
      * Use an array of dictionaries for storing frame information.
      * In that array, store Tk variables that are mapped to entries and labels
        as necessary.
      * Attach a magic "resolver" that will compute the scores.
    * OK, not as productive as I had imagined: how the hell do I implement the
      feature for jumping to the next entry?
      * I did shoot myself in the foot by not preserving references to the
        entries I created.
      * It is also complicated by nesting things in frames.
  * New day, new patience.
    * Good to learn that the default behavior in Tkinter on validation failure is
      to prevent a change in an entry.
      * Probably attributed to using the %P selector, which grabs the new value.
    * I'm looking at building a MVVM architecture.
      * MVC doesn't lend itself well to desktop applications in my experience.
      * Tkinter manages the core view, we provide a view model for frames that
        map the model frames to a usable view.
        * For speed, I might combine the model and view model into a single class
          so that I don't have to monkey too much with architecture and hopefully
          avoid more gotchas.
    * Instead of getting stuck trying to implement unit tests, I've opted to use
      Sikuli to verify that things are working as intended.
      * I would've used a Sikuli wrapper for Python to use it directly
        in unit tests, but I can't seem to get it to install properly on my
        machine.
      * Attempting to use the official Sikuli adapter for Python came with its
        complications. Required to orchestrate a background server alongside
        the tests.
      * Again, for speed, I'm just using Sikuli IDE.
    * OK, Sikuli is entertaining...
      * Had to decrease its tolerance for differences to prevent it from clicking
        on the wrong input field.
    * Ideas I'd love to try with testing and Sikuli:
      1. Provide arguments to AlleyGator to give it an initial state.
         * Would short-circuit having to use Sikuli to setup the state for the test.
      2. Integrate Sikuli into tests run by unittest.
         * Won't have to manually run every test, can run them in batches.
         * Don't have to read the output of every test to determine if a failure occurred.
      3. Per test recording.
         * Not 100% sure how to go about that, but I would love to just have footage
           to watch instead of running everything over and over again.
         * This was the premise of the Replay application I contributed to
           back in 2021, but for web applications.
         * The Benefit would be the easy sharing of test cases that illustrate
           what is going on.
      4. Parameterize tests to automate testing for each input.
         * Right now, I have to create an individual test for each input field,
           which makes the test suite even more fragile than it already is.
         * Reading the documentation for Sikuli, seems that this is what Regions
           would be used for.
           * Bingo. Got it working for the test that verifies digits can be
             input without issue.
           * Got to say it is satisfying watching this thing run.
    * Interesting observation about this visual testing:
      * It has me thinking about visual design from a testability perspective.
      * Since the software can be confused (quite easily sometimes) by visually
        indistinct elements, there's a fascinating application for accessibility
        testing.

---

```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
```
