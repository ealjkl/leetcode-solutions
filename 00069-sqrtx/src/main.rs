pub struct Solution {}

impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        let sqrt = (x as f32).sqrt();
        let pow = (sqrt as i32) * (sqrt as i32);
        if pow > x {
            return sqrt as i32 - 1;
        }
        sqrt as i32
    }
}

fn main() {
    let ans = Solution::my_sqrt(2147395599);
    println!("ans {}", ans);
}
