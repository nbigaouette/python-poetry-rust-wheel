#[derive(Debug)]
#[repr(C)]
pub struct Point {
    pub x: i32,
    pub y: i32,
}

#[no_mangle]
fn modify_point(mut p: Point) {
    let old_x = p.x;
    println!("From Rust: p: {:?}", p);
    p.x = (p.y + 1) * 2;
    p.y = (old_x - 5) * 3;
    println!("From Rust: p: {:?}", p);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let p = Point {x: 1, y: 2};
        modify_point(p);
    }
}
