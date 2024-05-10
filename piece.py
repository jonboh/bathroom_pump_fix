import solid2 as s
from solid2 import down, left

if __name__ == "__main__":
    cyl_outer = s.cylinder(h=21.5, r=19, _fn=200)
    cyl_inner = down(0.01)(s.cylinder(h=20, r=18, _fn=200))
    center_tube = down(0.01)(s.cylinder(h=22, r=7, _fn=200))
    notch = left(19)(s.cube(2, 3.5, 30))
    top_outer_top = s.difference()(s.cylinder(h=2.5, r=24, _fn=200), cyl_inner)
    top_outer_bottom = s.difference()(
        s.cylinder(h=5, r=24, _fn=200), down(0.01)(s.cylinder(h=5.5, r=22, _fn=200))
    )
    top = s.union()(top_outer_top, top_outer_bottom)
    main_body = s.difference()(cyl_outer, cyl_inner, center_tube, notch)

    piece = s.union()(top, main_body)
    s.scad_render_to_file(piece)
