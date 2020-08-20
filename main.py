class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2

def on_left_pressed():
    animation.run_image_animation(skemdo,
        [img("""
                . . . f f f f f . . . . 
                        . . f e e e e e f f . . 
                        . f e e e e e e e f f . 
                        f e e e e e e e f f f f 
                        f e e 4 e e e f f f f f 
                        f e e 4 4 e e e f f f f 
                        f f e 4 4 4 4 4 f f f f 
                        f f e 4 4 f f 4 e 4 f f 
                        . f f d d d d 4 d 4 f . 
                        . . f b b d d 4 f f f . 
                        . . f e 4 4 4 e e f . . 
                        . . f 1 1 1 e d d 4 . . 
                        . . f 1 1 1 e d d e . . 
                        . . f 6 6 6 f e e f . . 
                        . . . f f f f f f . . . 
                        . . . . . f f f . . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . . f e e e e e f f f . 
                        . f e e e e e e e f f f 
                        f e e e e e e e f f f f 
                        f e e 4 e e e f f f f f 
                        f e e 4 4 e e e f f f f 
                        f f e 4 4 1 1 4 f f f f 
                        . f e 4 4 f 1 4 e 4 f f 
                        . . f d d d d 4 d 4 f . 
                        . . f b b d e e f f f . 
                        . . f e 4 e d d 4 f . . 
                        . . f 1 1 e d d e f . . 
                        . f f 6 6 f e e f f f . 
                        . f f f f f f f f f f . 
                        . . f f f . . . f f . .
            """),
            img("""
                . . . f f f f f . . . . 
                        . . f e e e e e f f . . 
                        . f e e e e e e e f f . 
                        f e e e e e e e f f f f 
                        f e e 4 e e e f f f f f 
                        f e e 4 4 e e e f f f f 
                        f f e 4 4 4 4 4 f f f f 
                        f f e 4 4 f f 4 e 4 f f 
                        . f f d d d d 4 d 4 f . 
                        . . f b b d d 4 f f f . 
                        . . f e 4 4 4 e e f . . 
                        . . f 1 1 1 e d d 4 . . 
                        . . f 1 1 1 e d d e . . 
                        . . f 6 6 6 f e e f . . 
                        . . . f f f f f f . . . 
                        . . . . . f f f . . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . . f e e e e e f f f . 
                        . f e e e e e e e f f f 
                        f e e e e e e e f f f f 
                        f e e 4 e e e f f f f f 
                        f e e 4 4 e e e f f f f 
                        f f e 4 4 1 1 4 f f f f 
                        . f e 4 4 f 1 4 e 4 f f 
                        . . f d d d d 4 d 4 f f 
                        . . f b b d d 4 f f f . 
                        . . f e 4 4 4 e d d 4 . 
                        . . f 1 1 1 1 e d d e . 
                        . f f 6 6 6 6 f e e f . 
                        . f f f f f f f f f f . 
                        . . f f f . . . f f . .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    animation.run_image_animation(skemdo,
        [img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 4 4 4 4 4 4 e 4 f 
                        f 4 4 f f 4 4 f f 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """)],
        500,
        False)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.run_image_animation(skemdo,
        [img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 4 4 4 4 4 4 e 4 f 
                        f 4 4 f f 4 4 f f 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """),
            img("""
                . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 1 1 4 4 1 1 e 4 f 
                        f 4 4 1 f 4 4 f 1 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
            """)],
        500,
        False)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    animation.run_image_animation(skemdo,
        [img("""
                . . . . f f f f f . . . 
                        . . f f e e e e e f . . 
                        . f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 1 1 4 4 e f f 
                        f f 4 e 4 1 f 4 4 e f f 
                        . f 4 d 4 d d d d f f . 
                        . f f f 4 d d b b f . . 
                        . . f e e 4 4 4 e f . . 
                        . . 4 d d e 1 1 1 f . . 
                        . . e d d e 1 1 1 f . . 
                        . . f e e f 6 6 6 f . . 
                        . . . f f f f f f . . . 
                        . . . . f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . f f f e e e e e f . . 
                        f f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 4 4 4 4 e f f 
                        f f 4 e 4 f f 4 4 e f . 
                        . f 4 d 4 d d d d f . . 
                        . f f f e e d b b f . . 
                        . . f 4 d d e 4 e f . . 
                        . . f e d d e 1 1 f . . 
                        . f f f e e f 6 6 f f . 
                        . f f f f f f f f f f . 
                        . . f f . . . f f f . .
            """),
            img("""
                . . . . f f f f f . . . 
                        . . f f e e e e e f . . 
                        . f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 1 1 4 4 e f f 
                        f f 4 e 4 1 f 4 4 e f f 
                        . f 4 d 4 d d d d f f . 
                        . f f f 4 d d b b f . . 
                        . . f e e 4 4 4 e f . . 
                        . . 4 d d e 1 1 1 f . . 
                        . . e d d e 1 1 1 f . . 
                        . . f e e f 6 6 6 f . . 
                        . . . f f f f f f . . . 
                        . . . . f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . f f f e e e e e f . . 
                        f f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 4 4 4 4 e f f 
                        f f 4 e 4 f f 4 4 e f . 
                        f f 4 d 4 d d d d f . . 
                        . f f f 4 d d b b f . . 
                        . 4 d d e 4 4 4 e f . . 
                        . e d d e 1 1 1 1 f . . 
                        . f e e f 6 6 6 6 f f . 
                        . f f f f f f f f f f . 
                        . . f f . . . f f f . .
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_combos_attach_combo():
    animation.run_image_animation(skemdo,
        [img("""
                . . . . f f f f f . . . 
                        . . f f e e e e e f . . 
                        . f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 4 4 4 4 e f f 
                        f f 4 e 4 f f 4 4 e f f 
                        . f 4 d 4 d d d d f f . 
                        . f f f 4 d d b b f . . 
                        . . f e e 4 4 4 e f . . 
                        . . 4 d d e 1 1 1 f . . 
                        . . e d d e 1 1 1 f . . 
                        . . f e e f 6 6 6 f . . 
                        . . . f f f f f f . . . 
                        . . . . f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . f f f e e e e e f . . 
                        f f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 4 4 4 4 e f f 
                        f f 4 e 4 f f 4 4 e f . 
                        . f 4 d 4 d d d d f . . 
                        . f f f e e d b b f . . 
                        . . f 4 d d e 4 e f . . 
                        . . f e d d e 1 1 f . . 
                        . f f f e e f 6 6 f f . 
                        . f f f f f f f f f f . 
                        . . f f . . . f f f . .
            """),
            img("""
                . . . . f f f f f . . . 
                        . . f f e e e e e f . . 
                        . f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 4 4 4 4 e f f 
                        f f 4 e 4 f f 4 4 e f f 
                        . f 4 d 4 d d d d f f . 
                        . f f f 4 d d b b f . . 
                        . . f e e 4 4 4 e f . . 
                        . . 4 d d e 1 1 1 f . . 
                        . . e d d e 1 1 1 f . . 
                        . . f e e f 6 6 6 f . . 
                        . . . f f f f f f . . . 
                        . . . . f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . 
                        . . . f f f f f f . . . 
                        . f f f e e e e e f . . 
                        f f f e e e e e e e f . 
                        f f f f e e e e e e e f 
                        f f f f f e e e 4 e e f 
                        f f f f e e e 4 4 e e f 
                        f f f f 4 4 4 4 4 e f f 
                        f f 4 e 4 f f 4 4 e f . 
                        f f 4 d 4 d d d d f . . 
                        . f f f 4 d d b b f . . 
                        . 4 d d e 4 4 4 e f . . 
                        . e d d e 1 1 1 1 f . . 
                        . f e e f 6 6 6 6 f f . 
                        . f f f f f f f f f f . 
                        . . f f . . . f f f . .
            """)],
        100,
        True)
    skemdo.vx += 100
controller.combos.attach_combo("" + controller.combos.id_to_string(controller.combos.ID.RIGHT) + controller.combos.id_to_string(controller.combos.ID.PLUS) + controller.combos.id_to_string(controller.combos.ID.A),
    on_combos_attach_combo)

skemdo: Sprite = None
skemdo = sprites.create(img("""
        . . . . f f f f . . . . 
            . . f f e e e e f f . . 
            . f f e e e e e e f f . 
            f f f f 4 e e e f f f f 
            f f f 4 4 4 e e f f f f 
            f f f 4 4 4 4 e e f f f 
            f 4 e 4 4 4 4 4 4 e 4 f 
            f 4 4 f f 4 4 f f 4 4 f 
            f e 4 d d d d d d 4 e f 
            . f e d d b b d d e f . 
            . f f e 4 4 4 4 e f f . 
            e 4 f b 1 1 1 1 b f 4 e 
            4 d f 1 1 1 1 1 1 f d 4 
            4 4 f 6 6 6 6 6 6 f 4 4 
            . . . f f f f f f . . . 
            . . . f f . . f f . . .
    """),
    SpriteKind.player)
scene.set_background_image(img("""
    9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
        9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e 9 9 
        e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e 
        e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e 
        e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e d d d d d d d d d d d d d e e e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 d d d d d d d d d d d d d d d d d d d d e e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e 9 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e 9 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 d 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e e e 9 9 9 9 9 d d d d d d d d 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e e e 9 9 d d d d d d d d d d d 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e 9 9 9 9 e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e e e d d d d d d d d d d d d d 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e 9 9 e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e e e d d d d d d d d d d d d d 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e e e d d d d d d d d d d d d d d 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e e d d d d d d d d d d d d d d d d 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e d d d d d d d d d d d d d d d d d 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e e d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e 9 9 e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e 9 9 e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e 
        e e e d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e 
        e e d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e 
        e e d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e 
        e d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e 
        e d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e 
        e d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e d d d d d e e e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e 
        d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e d d d d d d d e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e d d d d d d d d e e e e e e e e e e e e e e 9 9 9 9 9 9 9 9 9 9 e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e 9 e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d e e e e d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e e e e e e e e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d e e e e e e d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
"""))
tiles.set_tilemap(tiles.create_tilemap(hex("""
            270008000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a0a000000000000000000000000000000000000000000000000000000000000000000000000000a0a000000000101010101010101010101010101010101010101010101010101010101010101010a0a0a0a01010202030202020202020302020302030202020203030203020202020203020202020a0a0a0a0202020303030303030203030303030302030302020303030303030303030203030303020302030303040505050505050505050505050505050505050505050505050505050505050505050505050507060909090909090909090909090909090909090909090909090909090909090909090909090908
        """),
        img("""
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 2 . . . . 
                . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 2 . . . . 
                . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 2 2 2 . . 
                . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 2 2 2 . . 
                . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        """),
        [myTiles.transparency16,
            myTiles.tile1,
            sprites.castle.tile_grass1,
            sprites.castle.tile_grass3,
            sprites.builtin.forest_tiles5,
            sprites.builtin.forest_tiles6,
            sprites.builtin.forest_tiles9,
            sprites.builtin.forest_tiles7,
            sprites.builtin.forest_tiles11,
            sprites.builtin.forest_tiles10,
            myTiles.tile2],
        TileScale.SIXTEEN))
controller.move_sprite(skemdo, 50, 0)
scene.camera_follow_sprite(skemdo)
statusbar = statusbars.create(20, 4, StatusBarKind.health)
statusbar.value = 100
statusbar.max = 100
statusbar.attach_to_sprite(skemdo, 7, 0)
statusbar.set_color(2, 1, 10)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . f f . . . . . . . 
            . . . . . . . . . . . . . f f 2 f f f f . . . . 
            . . . . . . . . . . . . f f 2 f e e e e f f . . 
            . . . . . . . . . . . f f 2 2 f e e e e e f f . 
            . . . . . . . . . . . f e e e e f f e e e e f . 
            . . . . . . . . . . f e 2 2 2 2 e e f f f f f . 
            . . . . . . . . . . f 2 e f f f f 2 2 2 e f f f 
            . . . . . . . . . . f f f e e e f f f f f f f f 
            . . . . . . . . . . f e e 4 4 f b e 4 4 e f e f 
            . . . . . . . . . . . f e d d f b 4 d 4 e e f . 
            . . . . . . . . . . c . e e d d d 4 e e e f . . 
            . . . . c c c c c c c e d d e e 2 2 2 2 f . . . 
            . . . . . d d d d d c e d d 4 4 e 4 4 4 f . . . 
            . . . . . . c c c c c . e e e e f f f f f . . . 
            . . . . . . . . . . c . . . f f f f f f f f . . 
            . . . . . . . . . . . . . . . f f . . f f f . . 
            . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
mySprite.set_position(51, 58)
mySprite.follow(skemdo, 20)

def on_update_interval():
    statusbar.value += 10
    print("Thats better")
    blockSettings.write_number("Save", 1)
game.on_update_interval(1000, on_update_interval)

def on_forever():
    if skemdo.overlaps_with(mySprite):
        statusbar.say("Oof")
        scene.camera_shake(2, 100)
        statusbar.value += -2.6
        print("Oof")
    if statusbar.value == 0:
        game.over(False, effects.splatter)
    if statusbar.value == 100:
        statusbar.say(":)", 100)
        print("I am all done!")
forever(on_forever)
