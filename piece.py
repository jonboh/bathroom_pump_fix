import solid2 as s
from solid2 import down, left

if __name__ == "__main__":
    cyl_outer = s.cylinder(h=23.5, r=19, _fn=200)
    cyl_inner = down(0.01)(s.cylinder(h=20, r=17.75, _fn=200))
    center_tube = down(0.01)(s.cylinder(h=25, r=7, _fn=200))
    center_tube_notch = s.up(21)(s.cylinder(10, r=10, _fn=200))
    notch = left(19)(s.cube(2, 3.5, 30))
    top_outer_top = s.difference()(s.cylinder(h=2.5, r=24, _fn=200), cyl_inner)
    top_outer_bottom = s.difference()(
        s.cylinder(h=5, r=24, _fn=200), down(0.01)(s.cylinder(h=5.5, r=22, _fn=200))
    )
    top = s.union()(top_outer_top, top_outer_bottom)
    main_body = s.difference()(
        cyl_outer, cyl_inner, center_tube, notch, center_tube_notch
    )

    piece = s.union()(top, main_body)
    s.scad_render_to_file(piece)

    outer_outer_d = 80
    inner_outer_d = 57
    rescue_hole_d = 33
    bottom_length = 20
    surface_thickness = 2
    weight = s.union()(
        s.difference()(
            s.cylinder(h=bottom_length, d=outer_outer_d, _fn=200),
            s.cylinder(h=bottom_length, d=inner_outer_d, _fn=200),
        ),
    )
    surface = s.down(surface_thickness)(
        s.difference()(
            s.cylinder(h=surface_thickness, d=outer_outer_d, _fn=200),
            s.cylinder(h=surface_thickness, d=rescue_hole_d, _fn=200),
        )
    )
    # weight_holder = s.union()(
    #     s.down(15)(s.cylinder(h=20, d=65)),
    # )
    # weight_holder = s.difference()(weight_holder, s.down(15)(s.cylinder(h=15, d=70)))
    shape = s.union()(weight, surface)
    s.scad_render_to_file(shape, filename="weight_holder.scad")
