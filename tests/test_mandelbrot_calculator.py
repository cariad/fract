from pytest import mark

from fract.mandelbrot_calculator import MandelbrotCalculator


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
    result = MandelbrotCalculator.count_iterations(
        real,
        imaginary,
        100,
    )

    assert result == expect


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
    result = MandelbrotCalculator.estimate_in_mandelbrot_set(
        real,
        imaginary,
    )

    assert result is expect
