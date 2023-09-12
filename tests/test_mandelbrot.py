from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory

from fract import render
from fract.mandelbrot import calculate_segment, iterations_to_pixels
from fract.process_instruction import ProcessInstruction
from fract.segment import Segment


def test_calculate_segment() -> None:
    result_byte_length = 1

    with NamedTemporaryFile() as f:
        instruction = ProcessInstruction(
            min_x=23,
            max_iterations=100,
            max_x=26,
            plane_min_x=-1.0,
            plane_width=2.0,
            plane_y=0.1,
            render_width=200,
            result_byte_length=result_byte_length,
            result_path=Path(f.name),
        )

        calculate_segment(instruction)

        f.seek(0)

        iterations: list[int] = []

        with open(f.name, "rb") as fr:
            while read_bytes := fr.read(result_byte_length):
                iterations.append(int.from_bytes(read_bytes))

        assert iterations == [100, 30, 32]


def test_iterations_to_pixels() -> None:
    max_iterations = 100
    result_byte_length = 1

    with TemporaryDirectory() as temp_dir:
        working_directory = Path(temp_dir)

        s1 = Segment(
            max_x=1,
            min_x=3,
            path=working_directory / "1",
            y=45,
        )

        s2 = Segment(
            max_x=3,
            min_x=6,
            path=working_directory / "2",
            y=45,
        )

        s3 = Segment(
            max_x=1,
            min_x=9,
            path=working_directory / "3",
            y=46,
        )

        with open(s1["path"], "wb") as f:
            f.write((100).to_bytes(result_byte_length))
            f.write((99).to_bytes(result_byte_length))

        with open(s2["path"], "wb") as f:
            f.write((0).to_bytes(result_byte_length))
            f.write((100).to_bytes(result_byte_length))

        with open(s3["path"], "wb") as f:
            f.write((0).to_bytes(result_byte_length))
            f.write((100).to_bytes(result_byte_length))
            f.write((0).to_bytes(result_byte_length))

        pixels = iterations_to_pixels(
            max_iterations,
            result_byte_length,
            iter([s1, s2, s3]),
        )

        assert list(pixels) == [
            [0, 0, 0, 255, 255, 255, 255, 255, 255, 0, 0, 0],
            [255, 255, 255, 0, 0, 0, 255, 255, 255],
        ]


def test_render() -> None:
    render(
        800,
        600,
        Path("docs") / "demo.png",
    )
