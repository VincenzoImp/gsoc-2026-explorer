# this
issue

**Parent:** SymPy — Project Ideas
**Source:** https://github.com/sympy/sympy/issues/20914
**Scraped:** 2026-02-22T23:28:47.573756

---

## Hypothesis testing

**Labels:** Testing

I'd like to use this issue to discuss the idea of using [hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html) in SymPy. 

For those who don't know, hypothesis is a library that lets you do property based testing. You tell it what the input to your function should look like and assert what properties should always hold, and it tries to find inputs that falsify that. Here's an example to show what a hypothesis test looks like

```py
from hypothesis import given
from hypothesis.strategies import integers

 @given(integers())
 def test_factorint(x):
     f = factorint(x)
     assert Mul(*[b**e for b, e in f.items()]) == x
     for b in f:
         assert abs(b) in [0, 1] or isprime(b)
```

(note that this test as written will fail because it takes too long for some inputs, but it's just to give the idea of what a property based test looks like)

Hypothesis is an extremely powerful tool. It is very good at finding examples that fail your tests, things which you would never think to test yourself. However, it's also very picky. As soon as it finds a failing test, it remembers it and always reports it. So it's only useful to add it to SymPy in a place where either the code currently works, or we are willing to fix any bugs that it finds.

There has been a lot of discussion on this in the past. See https://github.com/sympy/sympy/pull/17190 and https://github.com/sympy/sympy/pull/20906. 

My idea with hypothesis is to start small. Much smaller than what was proposed in https://github.com/sympy/sympy/pull/17190 (although that approach can still have some merits as something to run independently to see if anything interesting pops up). For example, the example test I wrote in https://github.com/sympy/sympy/pull/20906 passes on that branch. I just ran over 20000 examples. Even it, though, is still too much to start with, IMO, because the "correct" strategy to get it to find interesting examples is nontrivial. Random polynomials do not factor or have interesting roots. So you need to generate things in a way that matches what you are looking for. 

I'll have to think a bit on where a good place to start would be. Ideally it would be something that is easy to generate with the builtin hypothesis strategies, something that doesn't blow up in terms of performance on certain inputs, and something where interesting inputs aren't difficult to find from the naive way of generating them. 

The hardest part of writing good hypothesis tests is writing good strategies. But fortunately, strategies are reusable, so, e.g., if we created a good strategy for generating interesting expressions, then contributors would not need to worry about that to use it. Writing the test itself is generally straightforward. You just think of as many things as you want to be true of your function and assert them. It can be complicated, but not too hard once you get the hang of it. Actually, simply writing the test forces you to think about what you actually want to be true about your function (it is in some loose sense, a "spec" for your function). So insomuch as writing a property-based test is hard, that's a good thing.

[Here are some slides](https://speakerdeck.com/asmeurer/testing-with-hypothesis) for an presentation I gave internally to some colleagues about hypothesis. You can also take a look at the test suite for [ndindex](https://github.com/Quansight-Labs/ndindex), a library that I wrote, if you want to see what hypothesis tests look like in practice (see the [docs](https://quansight-labs.github.io/ndindex/#testing-and-correctness) for a high level description of how the tests work). 

