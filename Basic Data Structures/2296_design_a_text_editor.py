class TextEditor:

    def __init__(self):
        """
        One stack (“left”) will hold the characters to the left of the cursor,
        and the other (“right”) will hold the characters to the right of the cursor. This way, inserting, deleting, or moving the cursor can all be done in O(1) per character.
        """
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        # Add each character to the left stack.
        """
        O(T), len of text to add
        O(T)
        """
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        """
        O(min(k,N)), N num of chars in the left stack
        O(1)
        """
        deleted = 0
        while k > 0 and self.left:
            self.left.pop()
            deleted += 1
            k -= 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        """
        O(min(k,N)), N num of chars can be moved
        O(1)
        """
        # Move the cursor k positions to the left.
        # For each move, pop a character from the left stack and push it to the right stack.
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1
        # Return the last 10 characters to the left of the cursor.
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        """
        Same as above
        """
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1
        # Return the last 10 characters to the left of the cursor.
        return ''.join(self.left[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
