"""https://www.hackerrank.com/challenges/tree-huffman-decoding/problem"""

def huffman_decoding(root, s, result=""):
    """ This RECURSIVE SOLUTION *************   FAILS  ************"""
    if root.left is None and root.right is None:
        result = result + root.data

    else:
        if s[0] == "1":
            huffman_decoding(root.left, s[1:], result)
        if s[0] == "0":
            huffman_decoding(root.right, s[1:], result)

    return result




def decodeHuff(root, s):
   """Can you figure out the RECURSIVE VERSION of this solution?? Is there any????"""
   temp = root
   string = []
   for i in s:
       c = int(i)
       if c == 1:
           temp = temp.right
       elif c == 0:
           temp = temp.left
       if temp.right == None and temp.left == None:
           string.append(temp.data)
           temp = root
   b = "".join(string)

   print(b)