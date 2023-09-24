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
            docs / "down.png",
            imaginary=1,
        )

        calculator.enqueue(
            width,
            height,
            docs / "up.png",
            imaginary=-1,
        )

        calculator.enqueue(
            width,
            height,
            docs / "spike.png",
            real=-7.512161027228863343638453051344657940828e-01,
            imaginary=7.564322879586228138815367330951882912101e-02,
            real_span=2.525954765394997575123068990514486572846e-02,
        )

        calculator.enqueue(
            width,
            height,
            docs / "blob.png",
            real=-7.477206299701217857868874599694192861252e-01,
            imaginary=7.647562179933755900697580511712126156030e-02,
            real_span=4.789022958086932357423846003655134377124e-03,
        )
