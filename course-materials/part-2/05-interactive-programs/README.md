# Interactive Programs

## (If Time Permits) Large Example: Game of BORK

In the olden days, games were played on a text interface! Many an after-school hours were wasted on such games.

![](https://upload.wikimedia.org/wikipedia/en/a/ac/Zork_I_box_art.jpg)

One of the most famous was [Zork](https://en.wikipedia.org/wiki/Zork). You can play it in your web browser [here](https://textadventures.co.uk/games/play/5zyoqrsugeopel3ffhz_vq).

It's easy to write a game using all the knowledge we've learned so far!

The (very small) game world map looks like this, laid out on a standard [X/Y (i.e. Cartesian) coordinate system](https://en.wikipedia.org/wiki/Cartesian_coordinate_system):

```
    +----------+---------+---------+
 2  | Path     | Path    | Tractor |
    +----------+---------+---------+
 1  | Hut      | Corn    | Corn    |
    +----------+---------+---------+
 0  | Clearing | Corn    | Corn    |
    +----------+---------+---------+
         0          1         2
```

Under this coordinate system, the Hut (for example) would be located at the *xy* coordinates of (0,1) -- Luckily, these coordinates works perfectly as **indices** in a multi-level list structure!

Let's dissect this program and see how it works.

The source code is here: [bork.py](bork.py)