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
