See the README files in the folders (displayed on GitHub) for more information on each project.

## Testing
Using `pytest`: from the root directory, run `python -m pytest -s test/*`

## Notes
* Rewritten using Python 3.11.
* Some of the projects, and especially test files, use star import `from x import *` to import the module's entire namespace. This is often considered a bad practice, but in this case it's justified, since test utilities and configs in this project are specifically designed to be used with a star import.

## Interesting sources and videos:

* [Crash course computer science](https://youtu.be/tpIctyqH29Q) - if you liked nand2tetris, definitely check this out!
* [Online electronic circuit simulator](https://www.falstad.com/circuit/) - a very nice simulator on JS.
* [Simple CPU design](http://www.simplecpudesign.com) - check this out if you liked the hardware part of nand2tetris.