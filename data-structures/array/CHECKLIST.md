# Credit
Heavily inspired by [jwasham's coding interview university](https://github.com/jwasham/coding-interview-university). Slightly changed for my purposes.

# Progress
- [x] New raw data array with allocated memory
- [x] size() - number of items
- [x] capacity() - number of items it can hold
- [x] is_empty()
- [ ] at(index) - returns the item at a given index, throws error if out of bounds
- [ ] push(item)
- [ ] insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
- [ ] prepend(item) - can use insert above at index 0
- [x] append(item) - 
- [ ] pop() - remove from end, return value
- [ ] delete(index) - delete item at index, shifting all trailing elements left
- [ ] remove(item, occurances=-1) - looks for value and removes indexes holding it equal to num of occurances (-1 by default - all occurances)
- [ ] find(item) - looks for value and returns first index with that value, -1 if not found
- [ ] findall(item) - looks for value and returns all indexes with that valu
- [x] resize(new_capacity) // private function
    - when you reach capacity, resize to double the size
    - when popping an item, if the size is 1/4 of capacity, resize to half