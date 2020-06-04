from ctypes import CDLL, Structure, c_long

lib = CDLL("target/debug/libdfrs.dylib")

class Point(Structure):
    _fields_ = [
        ('x', c_long),
        ('y', c_long)
    ]


def run():
    p = Point(x=1, y=2)
    print(f"From python: p: ({p.x}, {p.y})")
    # This passes a copy of `p` to Rust. Original `p` stays intact.
    lib.modify_point(p)
    print(f"From python: p: ({p.x},{p.y})")
