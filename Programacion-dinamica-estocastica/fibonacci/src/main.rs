use std::collections::HashMap;

fn main() {
    
    let mut mem = HashMap::new();

    let mut input_text = String::new();

    println!("Elige un numero: ");
    std::io::stdin()
        .read_line(&mut input_text)
        .expect("failed to read from stdin");

    let trimmed = input_text.trim();
    
    match trimmed.parse::<u128>() {
        Ok(i) => {  let res = fibonacci_dinamico(i, &mut mem);
                    println!("El numero de fibonacci {} es {}", i, res);},
        Err(..) => println!("No es un numero"),
    };
}

fn fibonacci_dinamico(n: u128, memo: &mut HashMap<u128, u128>) -> u128 {
    if n == 1 || n == 0 {
        return 1;
    }

    let f = memo.get_key_value(&n);

    let f = match f {
        Some(n) => *n.1,
        None => {
                let resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo);
                memo.insert(n, resultado);
                return resultado
        },
    };

    return f;

}

fn fibonacci_recursivo(n: u128) -> u128 {
    if n == 1 || n == 0 {
        return 1;
    }

    fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
}
