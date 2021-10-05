let a = read_line();;
let a =  String.split_on_char ',' a;;
let b = List.map (String.trim) a;;
let numbers = List.map (int_of_string) b;;

let rec quick_sort = function
  | [] -> []
  | x::xs -> let left, right = List.partition (fun y -> y < x) xs
    in ( quick_sort left ) @ ( x::quick_sort right ) ;;

let result = quick_sort numbers;;
List.iter (fun x -> Printf.printf "%d " x) result ;;