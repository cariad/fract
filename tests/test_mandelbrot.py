from pathlib import Path

from fract import mandelbrot_calculator


def test_mandelbrot_calculator() -> None:
    docs = Path("docs")

    width = 800
    height = 600

    with mandelbrot_calculator() as calculator:
        calculator.enqueue(
            width,
            height,
            docs / "demo.png",
        )

        calculator.enqueue(
            width,
            height,
            docs / "bottom.png",
            imaginary=1.4,
        )

        calculator.enqueue(
            width,
            height,
            docs / "down.png",
            imaginary=1,
        )

        calculator.enqueue(
            width,
            height,
            docs / "top.png",
            imaginary=-1.4,
        )

        calculator.enqueue(
            width,
            height,
            docs / "up.png",
            imaginary=-1,
        )
