#![warn(
    clippy::all,
    clippy::pedantic,
    clippy::nursery,
    clippy::unwrap_used,
    clippy::expect_used
)]
#![allow(clippy::implicit_hasher)]

use color_eyre::Result;

fn main() -> Result<()> {
    color_eyre::install()?;

    println!("hello world 🦀");

    Ok(())
}
