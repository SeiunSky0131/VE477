(*I/O part*)
let node_num = read_int();;
let edge_num = read_int();;

type node = {
  mutable number : int;
  mutable in_degree : int;
  mutable out_list : int list;
};;

type edge = {
  mutable u: int;
  mutable v: int;
};;

let rec _init_edges_ l edge_size =
  match edge_size with
  | 0 -> l
  | _ -> let line = read_line() in
         let string_pair = String.split_on_char ' ' line in
         let int_pair = List.map (int_of_string) string_pair in
         let _u = List.nth int_pair 0 in
         let _v = List.nth int_pair 1 in
         let new_edge = {u = _u ; v = _v} in
         let l = l @ (new_edge::[]) in
         _init_edges_ l (edge_size-1);;

let rec _init_nodes_ l node_size =
  match node_size with
  | 0 -> l
  | _ -> let new_node = {number = node_size - 1 ; in_degree = 0; out_list = []} in
         let l = new_node::l in
         _init_nodes_ l (node_size-1);;

let rec increase_node_in_degree nodenum nodelist = 
  match nodelist with
  | [] -> ()
  | x::xs -> if x.number = nodenum then x.in_degree <- x.in_degree + 1
  else increase_node_in_degree nodenum xs;;

let rec decrease_node_in_degree nodenum nodelist = 
  match nodelist with 
  | [] -> ()
  | x::xs -> if x.number = nodenum then x.in_degree <- x.in_degree - 1
  else decrease_node_in_degree nodenum xs;;

let rec write_node_outlist nodenum out_node nodelist = 
  match nodelist with
  | [] -> ()
  | x::xs -> if x.number = nodenum then x.out_list <- out_node::x.out_list
  else write_node_outlist nodenum out_node xs;;

(*traverse the edgelist write the info for node with node_num*)
let rec write_info_per_node nodelist node_num edgelist = 
  match edgelist with
  | [] -> ()
  | x::xs -> if x.u = node_num then begin write_node_outlist node_num x.v nodelist; write_info_per_node nodelist node_num xs end
  else if x.v = node_num then begin increase_node_in_degree node_num nodelist; write_info_per_node nodelist node_num xs end
  else write_info_per_node nodelist node_num xs;;

let rec write_info nodelist edgelist node_size = 
  match node_size with 
  | 0 -> ()
  | _ -> write_info_per_node nodelist (node_size -1) edgelist; write_info nodelist edgelist (node_size-1);;


(*now we declare a node_list and a edge_list*)

let edge_list = _init_edges_ [] edge_num;;

let node_list = _init_nodes_ [] node_num;;

write_info node_list edge_list node_num;;

let queue = [];;

(*enqueue the number in the enqueuelist and make their in-degree to -1, return the updated queue*)
let rec enqueue enqueuelist queue nodelist =
  match enqueuelist with
  | [] -> queue
  | x::xs -> decrease_node_in_degree x.number nodelist; 
             let queue = queue @ (x::[]) in
             enqueue xs queue nodelist;;

(*deque the first element in the queue, return the updated queue, and the updated answer*)
let dequeue queue answer =
  match queue with
  | [] -> ([],answer)
  | x::xs -> (xs, answer @ (x ::[]));;


let queue = enqueue (List.filter (fun node -> node.in_degree = 0) node_list) queue node_list;;

let answer = [];;

(*This function update the node list according to the outlist of one node in the queue, the outlist should be the outlist of one node in the queue*)
let rec update_with_outlist outlist nodelist = 
  match outlist with
  | [] -> ()
  | x::xs -> decrease_node_in_degree x nodelist; update_with_outlist xs nodelist;;

let rec update queue node_list answer =
  match queue with
  | [] -> answer
  | x::xs -> let out_nodelist = x.out_list in
             update_with_outlist out_nodelist node_list; (*update its neighbors in the nodelist*)
             let (new_queue, new_answer) = dequeue queue answer in (*deque the queue and write the answer*)
             let queue = enqueue (List.filter (fun node -> node.in_degree = 0) node_list) new_queue node_list in  (*enqueue the new element into the queue*)
             update queue node_list new_answer;;

let answer = update queue node_list answer;;

let result = "";;
let rec print_answer answer size result =
  match size with
  | 1 -> let node = List.nth answer 0 in
        let result = result^(string_of_int node.number) in
        result
  | _ -> match answer with
  | [] -> ""
  | x::xs -> let result = result^ (string_of_int x.number) ^ " " in print_answer xs (size-1) result;;

let result = print_answer answer (List.length answer) result in
print_string result;;

             
