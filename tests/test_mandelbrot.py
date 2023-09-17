from pathlib import Path

from pytest import mark

from fract import render_mandelbrot
from fract.mandelbrot import count_iterations, estimate_in_mandelbrot_set


@mark.parametrize(
    "real, imaginary, expect",
    [
        (0, 0, 100),
        (
            -0.124999999999999555910790149937383830547332763671875,
            -0.854999999999999982236431605997495353221893310546875,
            100,
        ),
        (
            -0.252499999999999946709294817992486059665679931640625,
            -1.0725000000000000088817841970012523233890533447265625,
            6,
        ),
    ],
)
def test_count_iterations(
    real: float,
    imaginary: float,
    expect: int,
) -> None:
    assert count_iterations(real, imaginary, 100) == expect


@mark.parametrize(
    "real, imaginary, expect",
    [
        (0, 0, True),
        (-1, 0, True),
        (1, 1, False),
    ],
)
def test_estimate_in_mandelbrot_set(
    real: float,
    imaginary: float,
    expect: bool,
) -> None:
    assert estimate_in_mandelbrot_set(real, imaginary) is expect


def test_render() -> None:
    docs = Path("docs")

    width = 800
    height = 600

    render_mandelbrot(width, height, docs / "demo.png")
    render_mandelbrot(width, height, docs / "bottom.png", y=1.4)
    render_mandelbrot(width, height, docs / "down.png", y=1)
    render_mandelbrot(width, height, docs / "top.png", y=-1.4)
    render_mandelbrot(width, height, docs / "up.png", y=-1)
