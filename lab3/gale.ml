(*read in function*)
let rec read_in_line people l=
  match people with
  | 0 -> l
  | _ -> let list = read_line() in 
         let list = String.trim(list) in
         let list_ = String.split_on_char ' ' list in
         let _list_ = List.map (int_of_string) list_ in
         let l = l @ [_list_] in
         read_in_line (people-1) l;;

(*I/O part*)
let people = read_int();;
let man_prefer = read_in_line people [];;
let gap = read_line();; (*get rid of the gap line*)
let woman_prefer = read_in_line people [];;

(*I/O part, input correctness verification -> PASSED*)
(* let rec print_list lst =
  let cur_len = List.length lst in
    match lst with
    | [] -> ()
    | h::t -> match cur_len with 
    | 1 -> print_int h
    | _ -> print_int h; print_string ", "; print_list t;;

let rec print_list_list l =
  match l with
  | [] -> ()
  | x::xs ->
print_char '[';
print_list x  ;
print_char ']';
print_list_list xs;;

print_list_list man_prefer;;
print_list_list woman_prefer;; *)

(*kind of like a class*)
type person = {
  mutable number : int;
  mutable proposed_list : int list;
  mutable proposed : int;
  mutable lover : int;
};;

(*To reverse a list*)
let rev l =
  List.fold_left (fun a e -> e :: a) [] l;;

(*initialize the person*)
let _init_per tag list =
  let p = {number = tag ; proposed_list = list; proposed = -1; lover = -1} in p;;

let rec _init_ person_list people prefer_list = 
  match people with
  | 0 -> person_list
  | _ -> let p = _init_per (people-1) (List.nth prefer_list (people-1)) in
         let person_list = p::person_list in
         _init_ person_list (people - 1) prefer_list;;

(*These two lists perform like a structure array*)
let man_list = _init_ [] people man_prefer;;
let woman_list = _init_ [] people woman_prefer;;

(*some methods*)
let is_freeman list = 
  List.exists (fun p -> p.lover = -1) list;;

let is_freewoman list =
  List.exists (fun p -> p.lover = -1) list;;

let find_freeman list = 
  List.find (fun p -> p.lover = -1 ) list;;
  
let find_freewoman list = 
  List.find (fun p -> p.lover = -1) list;;

let find_woman_by_num list number =
  List.find (fun p -> p.number = number) list;;

let find_man_by_num list number = 
  List.find (fun p -> p.number = number) list;;

(*To use this function, you should input woman.proposed_list in the position 3, and put 0 for count, and put man nunber for man*)
let rec find_rank man count list =
  match list with
  | [] -> count
  | x::xs -> if x = man then count else find_rank man (count + 1) xs;;

(*This function will let man_p try woman_p, if fail return false, else return true*)
let try_woman man_p woman_p = 
  if woman_p.lover = -1 then true
  else let another_man_num = woman_p.lover in
       if find_rank man_p.number 0 woman_p.proposed_list < find_rank another_man_num 0 woman_p.proposed_list then true
       else false;;

let rec update_manlist man1 man_list_t =
  match man_list_t with
  | [] -> ()
  | x::xs -> if x.number = man1.number then x.lover <- man1.lover else update_manlist man1 xs;;

let rec update_manlist_attacker man1 man_list_t =
  match man_list_t with
  | [] -> ()
  | x::xs -> if x.number = man1.number then begin x.lover <- man1.lover; x.proposed <- x.proposed + 1 end
             else update_manlist_attacker man1 xs;;

let rec update_manlist_loser man1 man_list_t =
  match man_list_t with
  | [] -> ()
  | x::xs -> if x.number = man1.number then x.proposed <- x.proposed + 1
     else update_manlist_loser man1 xs;;

let rec update_womanlist woman1 woman_list_t =
  match woman_list_t with
  | [] -> ()
  | x::xs -> if x.number = woman1.number then x.lover <- woman1.lover else update_womanlist woman1 xs;;

let set_free man1 man2 woman =
  let man_1 = {number = man1.number; proposed_list = man1.proposed_list; proposed = man1.proposed; lover = woman.number} in
  let man_2 = {number = man2.number; proposed_list = man2.proposed_list; proposed = man2.proposed; lover = -1} in
  let woman_1 = {number = woman.number; proposed_list = woman.proposed_list; proposed = woman.proposed; lover = man1.number} in
  (man_1,man_2, woman_1);;

(*algorithm part*)
let rec marriage man_list_t woman_list_t = 
  if is_freeman man_list_t = false then () (*if there is no free man, we are done with input lists to be answer*)
  else 
    let freeman = find_freeman man_list_t in  (*find a freeman*)
    let proposed_woman_num = List.nth freeman.proposed_list (freeman.proposed + 1) in (*next woman that the man hasn't proposed yet*)
    let proposed_woman = find_woman_by_num woman_list_t proposed_woman_num in
      if proposed_woman.lover = -1 then (*if the proposed woman is free then we set them as pair and enter next loop*)
        let man1 = {number = freeman.number; proposed_list = freeman.proposed_list; proposed = freeman.proposed; lover = proposed_woman_num} in
        let woman1 = {number = proposed_woman_num; proposed_list = proposed_woman.proposed_list; proposed = proposed_woman.proposed; lover = freeman.number} in
        update_manlist_attacker man1 man_list_t; update_womanlist woman1 woman_list_t; marriage man_list_t woman_list_t
        
      else (*if the proposed woman is not free, we look for current date*)
        let another_man = find_man_by_num man_list_t  proposed_woman.lover in (*find the current date*)
        let willing = try_woman freeman proposed_woman in 
          if willing = true then (*if the woman is willing to marry the new man*)
            let (man1,man2,woman_1) = set_free freeman another_man proposed_woman in 
            update_manlist_attacker man1 man_list_t; update_manlist man2 man_list_t; update_womanlist woman_1 woman_list_t; marriage man_list_t woman_list_t (*then we set the new pairs and free the original man and enter next loop*)
          else (*if the woman prefer the original one*)
            update_manlist_loser freeman man_list_t;marriage man_list_t woman_list_t;; 


(*I/O part, input correctness verification -> PASSED*)
(* let rec print_list lst =
  let cur_len = List.length lst in
    match lst with
    | [] -> ()
    | h::t -> match cur_len with 
    | 1 -> print_int h
    | _ -> print_int h; print_string ", "; print_list t;;

let rec print_list_list l =
  match l with
  | [] -> ()
  | x::xs ->
print_char '[';
print_list x  ;
print_char ']';
print_list_list xs;;

print_list_list man_prefer;;
print_list_list woman_prefer;; *)

marriage man_list woman_list;;

let print_person h = 
    print_char '['; print_int h.number; print_string ", "; print_int h.lover; print_char ']';;

let rec print_all l cur_len=
  match l with
  | [] -> ()
  | x::xs -> match cur_len with 
            | 1 -> print_person x;
            | _ -> print_person x; print_string ", "; print_all xs (cur_len-1) ;;



print_char '[';
print_all man_list (List.length man_list);;
print_char ']';