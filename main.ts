controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (info.score() <= 14) {
        game.setDialogTextColor(7)
        game.setDialogCursor(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 7 7 . . . . . . . . . 
            . . . . . . . 7 7 . . . . . . . 
            . . . . . . . . . 7 7 . . . . . 
            . . . . . . . . . . . 7 7 . . . 
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . 
            . . . . . . . . . . . 7 7 . . . 
            . . . . . . . . . 7 7 . . . . . 
            . . . . . . . 7 7 . . . . . . . 
            . . . . . 7 7 . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `)
        game.setDialogFrame(img`
            5 5 5 f 5 f 5 f 5 f 5 f 5 5 5 
            5 f f f f f f f f f f f f f 5 
            5 f f f f f f f f f f f f f 5 
            f f f f f f f f f f f f f f f 
            5 f f f f f f f f f f f f f 5 
            f f f f f f f f f f f f f f f 
            5 f f f f f f f f f f f f f 5 
            f f f f f f f f f f f f f f f 
            5 f f f f f f f f f f f f f 5 
            f f f f f f f f f f f f f f f 
            5 f f f f f f f f f f f f f 5 
            f f f f f f f f f f f f f f f 
            5 f f f f f f f f f f f f f 5 
            5 f f f f f f f f f f f f f 5 
            5 5 5 f 5 f 5 f 5 f 5 f 5 5 5 
            `)
        game.showLongText("You don't have enough DJ bucks to build a house.   you need 15 DJ bucks to build one", DialogLayout.Full)
    } else if (info.score() >= 15) {
        if (house_built == false) {
            game.setDialogTextColor(7)
            game.setDialogCursor(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . 7 7 . . . . . . . . . 
                . . . . . . . 7 7 . . . . . . . 
                . . . . . . . . . 7 7 . . . . . 
                . . . . . . . . . . . 7 7 . . . 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . 
                . . . . . . . . . . . 7 7 . . . 
                . . . . . . . . . 7 7 . . . . . 
                . . . . . . . 7 7 . . . . . . . 
                . . . . . 7 7 . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `)
            game.setDialogFrame(img`
                5 5 5 f 5 f 5 f 5 f 5 f 5 5 5 
                5 f f f f f f f f f f f f f 5 
                5 f f f f f f f f f f f f f 5 
                f f f f f f f f f f f f f f f 
                5 f f f f f f f f f f f f f 5 
                f f f f f f f f f f f f f f f 
                5 f f f f f f f f f f f f f 5 
                f f f f f f f f f f f f f f f 
                5 f f f f f f f f f f f f f 5 
                f f f f f f f f f f f f f f f 
                5 f f f f f f f f f f f f f 5 
                f f f f f f f f f f f f f f f 
                5 f f f f f f f f f f f f f 5 
                5 f f f f f f f f f f f f f 5 
                5 5 5 f 5 f 5 f 5 f 5 f 5 5 5 
                `)
            effects.confetti.startScreenEffect(500)
            game.showLongText("WOW! You have enough DJ bucks! nice... ", DialogLayout.Full)
            info.changeScoreBy(10)
            tiles.setTilemap(tiles.createTilemap(hex`640008000b0d0d0d0d0d0d0d0d0d0b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000b0d0d0d0d0d0d0d0d0d0b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000b0d0d0d0d0d0d0d0d0d0b000000000000000000000000000000000000000000000000000000000a0000000a00000a00000a0000000a0000000a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000b0c0c0c0c0c0c0c0c0c0f010101010101010101010101010101010101010101010101010101010a0a010a0a0a0a0a0a010a0a01010a0a01010a0a0a0a0a01010101010101010101010101010101010101010101010101010101010101010000100010000e0e030e0e030303030303020302030202020203030203020202020203020202020e02020202020a0a020a0a0a0a0a0a020a0a02020a0a02020a0a0a0a0a02020202020202030303030303020202020202020303020202030303030303111010101010100203030303030302030303030303020303020203030303030303030302030303030203020303030e0e0e02020202020e0e030e020202020202020303020202020202020303030303030202020202020202030303030203030303030311101010101010100405050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050706090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090908`, img`
                2.........2.........................................................................................
                22222222222.........................................................................................
                2.........2............................2...2..2..2...2...2..........................................
                2......................................22.222222.22..22..22222......................................
                2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
                2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
                2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
                ....................................................................................................
                `, [myTiles.transparency16,myTiles.tile1,sprites.castle.tileGrass1,sprites.castle.tileGrass3,sprites.builtin.forestTiles5,sprites.builtin.forestTiles6,sprites.builtin.forestTiles9,sprites.builtin.forestTiles7,sprites.builtin.forestTiles11,sprites.builtin.forestTiles10,myTiles.tile2,myTiles.tile3,myTiles.tile4,myTiles.tile5,sprites.castle.tileGrass2,myTiles.tile7,myTiles.tile8,myTiles.tile9], TileScale.Sixteen))
            skemdo.setPosition(80, 55)
            house_built = true
            controller.moveSprite(skemdo, 50, 50)
            skemdo.ay = 150
        }
    }
})
scene.onHitWall(SpriteKind.Player, function (sprite, location) {
    if (controller.A.isPressed()) {
        tiles.setWallAt(location, false)
        tiles.setTileAt(location, myTiles.tile1)
        info.changeScoreBy(2)
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    skemdo.vy = -100
    skemdo.vy = 100
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    skemdo,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    skemdo,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    false
    )
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    animation.runImageAnimation(
    skemdo,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    false
    )
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    skemdo,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile7, function (sprite, location) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location, true)
        tiles.setTileAt(location, myTiles.tile6)
        info.changeScoreBy(1)
    }
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile6, function (sprite, location) {
    if (controller.B.isPressed()) {
        tiles.setWallAt(location, false)
        tiles.setTileAt(location, myTiles.tile7)
        info.changeScoreBy(1)
    }
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    game.setDialogTextColor(7)
    game.setDialogCursor(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . 7 7 . . . . . . . . . 
        . . . . . . . 7 7 . . . . . . . 
        . . . . . . . . . 7 7 . . . . . 
        . . . . . . . . . . . 7 7 . . . 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . 
        . . . . . . . . . . . 7 7 . . . 
        . . . . . . . . . 7 7 . . . . . 
        . . . . . . . 7 7 . . . . . . . 
        . . . . . 7 7 . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `)
    game.setDialogFrame(img`
        5 5 5 f 5 f 5 f 5 f 5 f 5 5 5 
        5 f f f f f f f f f f f f f 5 
        5 f f f f f f f f f f f f f 5 
        f f f f f f f f f f f f f f f 
        5 f f f f f f f f f f f f f 5 
        f f f f f f f f f f f f f f f 
        5 f f f f f f f f f f f f f 5 
        f f f f f f f f f f f f f f f 
        5 f f f f f f f f f f f f f 5 
        f f f f f f f f f f f f f f f 
        5 f f f f f f f f f f f f f 5 
        f f f f f f f f f f f f f f f 
        5 f f f f f f f f f f f f f 5 
        5 f f f f f f f f f f f f f 5 
        5 5 5 f 5 f 5 f 5 f 5 f 5 5 5 
        `)
    game.showLongText("You don't have enough DJ bucks to build a portal.   you need 150 DJ bucks to build one", DialogLayout.Full)
})
let house_built = false
let skemdo: Sprite = null
class ActionKind {
    static Walking = 0
    static Idle = 1
    static Jumping = 2
}
skemdo = sprites.create(img`
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
    `, SpriteKind.Player)
scene.setBackgroundImage(img`
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999ee999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999eeee99999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999eeee99999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999eeeee9999999999999999999999999999999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999999999999999999999eeeeee9999999999999999999999999999999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999999999999999999999eeeeee9999999999999999999999999999999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999999999999999999999eeeeee9999999999999999999999999999999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999999999999999999999eeeeee9999999999999999999999999999999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999999999999999999999eeeeee9999999999999999999999999999999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeee9999999999999999999999999999999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeee9999999999999999999999999999999999999999999999999999999999eeeeeeeeee99
    ee999999999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeeee99999999999999999999999999999999999999999999999999999999eeeeeeeeeeeee
    eeeee999999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeeee9999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeee
    eeeeee99999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeeee9999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeee
    eeeeeee9999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeeee9999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeee
    eeeeeee9999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeeee999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeee
    eeeeeee9999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeeee99999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeee
    eeeeeee9999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeeeee999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeee
    eeeeeee9999999999999999999999999999999999999999999999999999999999999999999999999999eeeeeeeee999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeee
    eeeeeee999999999999999999999999999999999eee9999999999999999999999999999999999999999eeeeeeeee999999999999999999999999999999999999999999999eedddddddddddddeeeeeeee
    eeeeeee999999999999999999999999999999eeeeeee999999999999999999999999999999999999999eeeeeeeeee9999999999999999999999999999999999999999ddddddddddddddddddddeeeeeee
    eeeeeee9999999999999999999999999999eeeeeeeee999999999999999999999999999999999999999eeeeeeeeee9999999999999999999999999999999999999ddddddddddddddddddddddddeeeeee
    eeeeeee99999999999999999999999999eeeeeeeeeeee99999999999999999999999999999999999999eeeeeeeeeee9999999999999dddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeeee9999999999999999999999999eeeeeeeeeeeee9999999999999999999999999999999999999eeeeeeeeeeee9dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeeee999999999999999999999999eeeeeeeeeeeeee999999999999999999999999999999999999eeeeeeeeeeeee9dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeeee99999999999d999999999999eeeeeeeeeeeeee999999999999999999999999999999999999eeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeeee99999dddddddd99999999999eeeeeeeeeeeeee999999999999999999999999ee999999999eeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeeee99ddddddddddd99999999999eeeeeeeeeeeeeee9999999999999999999999eeeeeee9999eeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeeeeddddddddddddd9999999999eeeeeeeeeeeeeeee999999999999999999999eeeeeeeeee99eeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeeeeddddddddddddd9999999999eeeeeeeeeeeeeeee999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeeeedddddddddddddd999999999eeeeeeeeeeeeeeee999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeedddddddddddddddd999999999eeeeeeeeeeeeeeee99999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeeddddddddddddddddd999999eeeeeeeeeeeeeeeeeee99999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeedddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeee99eee999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeee99eeee99999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeee
    eeeddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999eeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeee
    eedddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999eeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeee
    eedddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999eeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeee
    eddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999eeeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeee
    eddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999eeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeee
    eddddddddddddddddddddeeeeeeeeeeeedddddeeeeeeeeeeeeeeee99999999999eeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeee
    ddddddddddddddddddddddeeeeeeeeeeedddddddeeeeeeeeeeeeee99999999999eeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ddddddddddddddddddddddeeeeeeeeeeddddddddeeeeeeeeeeeeee9999999999eeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddeeeeeeedddddddddddeeeeeeeeeeeeeeeeeeeeee9eeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddeeeeddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    `)
tiles.setTilemap(tiles.createTilemap(hex`31000800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a0a000000000000000000000a0000000000000000000000000000000000000000000000000000000000000000000000000a0a00000000000a0a0a000a0a0000000101010101010101010101010101010101010101010101010101010101010101010a0a0a0a0101010a0a0a0a0a0a0a0a010202030202020202020302020302030202020203030203020202020203020202020a0a0a0a02020b0a0a0a0a0a0a0a0a0a0203030303030302030303030303020303020203030303030303030302030303030203020303030b0202030202030202030405050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050706090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090908`, img`
    .................................................
    .................................22..........2...
    .................................22.....222.22...
    .................................2222...22222222.
    2222222222222222222222222222222222222222222222222
    2222222222222222222222222222222222222222222222222
    2222222222222222222222222222222222222222222222222
    .................................................
    `, [myTiles.transparency16,myTiles.tile1,sprites.castle.tileGrass1,sprites.castle.tileGrass3,sprites.builtin.forestTiles5,sprites.builtin.forestTiles6,sprites.builtin.forestTiles9,sprites.builtin.forestTiles7,sprites.builtin.forestTiles11,sprites.builtin.forestTiles10,myTiles.tile2,sprites.castle.tileGrass2], TileScale.Sixteen))
controller.moveSprite(skemdo, 50, 0)
scene.cameraFollowSprite(skemdo)
let statusbar = statusbars.create(20, 4, StatusBarKind.Health)
statusbar.value = 100
statusbar.max = 100
statusbar.attachToSprite(skemdo, 7, 0)
statusbar.setColor(2, 1, 10)
let mySprite = sprites.create(img`
    ...............ff.......
    .............ff2ffff....
    ............ff2feeeeff..
    ...........ff22feeeeeff.
    ...........feeeeffeeeef.
    ..........fe2222eefffff.
    ..........f2effff222efff
    ..........fffeeeffffffff
    ..........fee44fbe44efef
    ...........feddfb4d4eef.
    ..........c.eeddd4eeef..
    ....ccccccceddee2222f...
    .....dddddcedd44e444f...
    ......ccccc.eeeefffff...
    ..........c...ffffffff..
    ...............ff..fff..
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    `, SpriteKind.Enemy)
if (!(blockSettings.exists("x")) && !(blockSettings.exists("y"))) {
    mySprite.setPosition(51, 58)
    mySprite.follow(skemdo, 20)
    skemdo.setFlag(SpriteFlag.ShowPhysics, true)
    skemdo.setPosition(80, 55)
    skemdo.ay = 220
} else {
    skemdo.setPosition(blockSettings.readNumber("x"), blockSettings.readNumber("y"))
}
game.onUpdate(function () {
    blockSettings.writeNumber("x", skemdo.x)
    blockSettings.writeNumber("y", skemdo.x)
})
game.onUpdateInterval(1000, function () {
    statusbar.value += 10
    console.log("Thats better")
    blockSettings.writeNumber("Save", 1)
})
forever(function () {
    if (skemdo.overlapsWith(mySprite)) {
        statusbar.say("Oof")
        scene.cameraShake(2, 100)
        statusbar.value += -2.6
        console.log("Oof")
    }
    if (statusbar.value == 0) {
        game.over(false, effects.dissolve)
    }
    if (statusbar.value == 100) {
        statusbar.say(":)", 100)
        console.log("I am all done!")
    }
})
