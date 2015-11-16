# Victor ![](https://travis-ci.org/jcomo/victor.svg?branch=master)
A small library for profiling and debugging python applications and functions. Inspired by [Hugo](https://github.com/JakeWharton/hugo).

### Usage

```sh
pip install victor
```

To debug a function, add a decorator. Whenever the function is run, Victor will spit out profiling and debugging information including the arguments it received, its return value, and the time it took to execute.

```python
from victor import debug


@debug
def greet(first, last):
  time.sleep(0.02)
  return "Hello, %s %s!" % (first, last)


if __name__ == '__main__':
  greet("Jonathan", "Como")
```

Running this program will produce the following output

```
2015-11-15 23:26:46,405 victor [DEBUG] -> greet('Jonathan', 'Como')
2015-11-15 23:26:46,430 victor [DEBUG] <- greet [24.87ms] => 'Hello, Jonathan Como!'
```

And that's about it (`with` feature coming soon). There are a couple of ways to customize Victor depending on your needs.

#### Disabling
The nice feature about Victor is that you can leave the debug decorators in the source code. It will not profile your production code when disabled.
To disable profiling, set the following property

```python
# Program initialization...
victor.enabled = False  # Better - read this from the environment or configuration
```

Note that since debug is a decorator, it will wrap the function. Disabling Victor simply means that the function will not be wrapped with profiling information.
Therefore, it is critical that the enabled property is set as soon as possible during app initialization so that modules aren't loaded (causing functions to be wrapped mistakenly).

#### BYOLogger
By default, Victor will log to stdout wiht a specific format. If you don't like that, you can assign your own logger using `victor.logger`.

#### Formatting the profiler
If you'd like more pizazz out of the profiling information, you can define your own `Presenter` with `view_input` and `view_output` that each return strings.
It doesn't necessarily have to subclass the default one, but if you'd like to override one method only then it might be useful to subclass instead.

```python
class MyPresenter(object):
  def view_input(self, f, *args, **kwargs):
    pass
      
  def view_output(self, f, result, elapsed_ms):
    pass
```
