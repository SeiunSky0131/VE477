let a = read_line();;
let a =  String.split_on_char ' ' a;;
let l = List.map (int_of_string) a;;

let ret_leq a b =
    if a>b then ([b],1) else ([a],0);;

(*input two lists and an indicator, return the list pair after modify and if we modify the right one, we need add the len of left*)
let ret_tail list1 list2 indicator =
if indicator = 0 then
   match list1 with 
        | [] -> ([],list2 , 0)
        | x::xs -> (xs,list2, 0)
else match list2 with
        | [] -> (list1, [], (List.length list1))
        | x::xs -> (list1, xs, (List.length list1))

(*To merge two part, you should input mergeCount_helper [] left right 0*)
let rec mergeCount_helper result_list l_list r_list count =
  match l_list with
  | [] -> (result_list @ r_list, count)
  | x1::xs1 -> match r_list with
  | [] -> (result_list @ l_list, count)
  | x2::xs2 -> let (elem,num) = ret_leq x1 x2 in
                let (l_list, r_list , adder) = ret_tail l_list r_list num in
                  (mergeCount_helper (result_list @ elem) l_list r_list (count + adder));;

(*To split a list, you should input mysplit [] list size_of_list size_of_list*)
let rec mysplit curr_arr l len curr_len =
  match l with
  | [] -> ([],[])
  | x::xs -> match curr_len with
  | t when t = len/2 -> (curr_arr,l)
  | _ -> let x = x::[] in 
          let curr_arr = curr_arr @ x in
            mysplit curr_arr xs len (curr_len - 1);;

let rec sortCount l =
  let len = List.length l in
    if len = 1 then (0,l) else
        let (left, right) = mysplit [] l len len in 
          let (count1, left) = sortCount left in
          let (count2, right) = sortCount right in
              let (all, count) = mergeCount_helper [] left right (count1 + count2) in
                (count, all);;

                
let rec print_list lst =
  let cur_len = List.length lst in
    match lst with
    | [] -> ()
    | h::t -> match cur_len with 
    | 1 -> print_int h
    | _ -> print_int h; print_string ", "; print_list t;;
              

let (count, result) =  sortCount l in
  Printf.printf "%d\n" count;;
print_char '[';;
let (count, result) =  sortCount l in
      print_list result ;;
print_char ']'