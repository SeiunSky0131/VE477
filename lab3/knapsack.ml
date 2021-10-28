let upper_bound = read_int();;

let num_list = String.split_on_char ' ' (read_line());;
let num_list = List.map (int_of_string) num_list;;

let n = List.length num_list;;

(*create a two dimension array and mark all of the buckets to be []*)
let rec _init_row_ row s_num =
  match s_num with
  | 0 -> row
  | _ -> let row = []::row in
         _init_row_ row (s_num - 1);; 

let rec _init_ table s_num i_num =
  match i_num with
  | 0 -> table
  | _ -> let new_row = _init_row_ [] s_num in
         let table = new_row::table in
         _init_ table s_num (i_num -1);;

let two_dem_table = _init_ [] (upper_bound+1) (n+1);;

let rec nth_partition n list = 
  match n with
  | 0 -> ([], list)
  | _ -> match list with
  | [] -> ([],[])
  | head::rest -> let (left, right) = nth_partition (n-1) rest in
    (head::left, right);;

(*update the mth value of a list*)
let update_mth list m value =
  match m with
  | m when m >= (List.length list)-> failwith "update mth value of the list"
  | _ -> let (front, back_with_target) = nth_partition m list in
    let (mth, back) = nth_partition 1 back_with_target in
      front @ (value::back);;

(*calculate the value of the bucket i,s*)
let rec q i s num_list = 
  if s <= 0 then []
  else
  match i with
  | 0 -> []
  | _ -> if s - (List.nth num_list (i-1)) = 0 then (List.nth num_list (i -1))::[]
         else
         let list1 = q (i - 1) s num_list in
         let list2 = q (i - 1) (s - List.nth num_list (i -1)) num_list in
         if list1 = [] then 
            if list2 = [] then [] else list2 @ ((List.nth num_list (i -1))::[])
          else list1;;

(*update the bucket i,s, the row should be the target row the ori_table should be the table, the cur_row should be zero*)
let rec update_row cur_row i s row ori_table num_list =
  match cur_row with
  | t when t = s + 1 -> row
  | _ ->  
          let value = q i cur_row num_list in
          let result = update_mth row cur_row value in
            update_row (cur_row+1) i s result ori_table num_list;;
         

let rec updateall cur_col table i_num s_num num_list =
  match cur_col with
  | t when t = i_num + 1-> table
  | _ -> let ori_row = List.nth table cur_col in
         let new_row = update_row 0 cur_col s_num ori_row table num_list in
         let new_table = update_mth table cur_col new_row in
         updateall (cur_col+1) new_table i_num s_num num_list;;

let two_dem_table = updateall 0 two_dem_table n upper_bound num_list;;

let final_row = List.nth two_dem_table n;;
let final_bucket = List.nth final_row upper_bound;;
let final_bucket = List.sort compare final_bucket;;

let rec print_list lst =
  let cur_len = List.length lst in
    match lst with
    | [] -> ()
    | h::t -> match cur_len with 
    | 1 -> print_int h
    | _ -> print_int h; print_string ", "; print_list t;;
              
(* print_char '[';;
      print_list result ;;
print_char ']' *)

let printall lst =
  match List.length lst with
  | 0 -> print_char '\n'
  | _ -> print_char '['; print_list lst; print_char ']';;

let print_with_input_check upper_bound final_bucket=
  match upper_bound with
  | 0 -> print_endline "[]\n"
  | _ -> printall final_bucket;;

print_with_input_check upper_bound final_bucket;;
