mod borrachos {
    mod borrachoComun {
        pub struct BorrachoComun {
            name: String,
        }

            pub fn new() -> BorrachoComun {
                BorrachoComun {
                    name: String::new(),
                }
            }

            pub fn init(borracho: &mut BorrachoComun, name: &str) -> &BorrachoComun {
                borracho.name.push_str(name);

                borracho
            }
    }
}

fn main() {
    println!("Hello, world!");
}
