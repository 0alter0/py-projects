// i did rust to spice it up. the best way to run it is to run rustc maze.rs then .\maze.exe
// rust is also way faster at making the bigger mazes than python so thats the other reason
use std::fs::File;
use std::io::{self, Write};

const W: usize = 1000;
const H: usize = 1000;

fn rand(seed: &mut u64, n: usize) -> usize {
    *seed ^= *seed << 13;
    *seed ^= *seed >> 7;
    *seed ^= *seed << 17;
    (*seed as usize) % n
}

fn main() -> io::Result<()> {
    let mut maze = vec![vec![false; W]; H];
    let mut stack = vec![(1usize, 1usize)];
    let mut seed = 123456789u64;

    maze[1][1] = true;

    while let Some(&(x, y)) = stack.last() {
        let mut n = [(0usize, 0usize); 4];
        let mut count = 0;

        if x >= 3 && !maze[y][x - 2] {
            n[count] = (x - 2, y);
            count += 1;
        }
        if x + 2 < W && !maze[y][x + 2] {
            n[count] = (x + 2, y);
            count += 1;
        }
        if y >= 3 && !maze[y - 2][x] {
            n[count] = (x, y - 2);
            count += 1;
        }
        if y + 2 < H && !maze[y + 2][x] {
            n[count] = (x, y + 2);
            count += 1;
        }

        if count == 0 {
            stack.pop();
            continue;
        }

        let (nx, ny) = n[rand(&mut seed, count)];
        maze[(y + ny) / 2][(x + nx) / 2] = true;
        maze[ny][nx] = true;
        stack.push((nx, ny));
    }

    maze[1][0] = true;
    maze[H - 2][W - 1] = true;

    let mut f = File::create("maze.bmp")?;

    let row_size = (W * 3 + 3) & !3;
    let image_size = row_size * H;
    let file_size = 54 + image_size;

    f.write_all(b"BM")?;
    f.write_all(&(file_size as u32).to_le_bytes())?;
    f.write_all(&[0; 4])?;
    f.write_all(&(54u32).to_le_bytes())?;

    f.write_all(&(40u32).to_le_bytes())?;
    f.write_all(&(W as i32).to_le_bytes())?;
    f.write_all(&(H as i32).to_le_bytes())?;
    f.write_all(&(1u16).to_le_bytes())?;
    f.write_all(&(24u16).to_le_bytes())?;
    f.write_all(&[0; 4])?;
    f.write_all(&(image_size as u32).to_le_bytes())?;
    f.write_all(&[0; 16])?;

    let padding = vec![0u8; row_size - W * 3];

    for y in (0..H).rev() {
        for x in 0..W {
            let c = if maze[y][x] { 255 } else { 0 };
            f.write_all(&[c, c, c])?;
        }
        f.write_all(&padding)?;
    }

    println!("Generated maze.bmp");
    Ok(())
}
