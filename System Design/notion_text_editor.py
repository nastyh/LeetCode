"""
At the core of Notion’s product, we have a text editor that allows text editing + collaboration. Today, we will be building a system that supports some of the key user operations/edits that a user can take on a basic Notion page with text.

We would like to build a TextDocument class that supports basic insertion and deletion operations of plain text with some basic undo-redo functionality.

Here is the expected structure for the operations:

/**
 * To start, we'll implement two types of operations we'd like to implement:
 * 1) InsertAtEndOperation: this will allow a user to append a string to the end
 *    of the document.
 * 2) DeleteFromEndOperation: this will allow a user to delete the last n chars
 *    from the document.
 */
type InsertAtEndOperation = {
    type: "insertAtEnd",
    charsToInsert: string
}

type DeleteFromEndOperation = {
    type: "deleteFromEnd",
    numCharsToDelete: number
}

type Operation = InsertAtEndOperation | DeleteFromEndOperation
Here's the structure for the TextDocument class we would like to build. We would like to implement the following 4 methods:

/**
 * Applies the given operation to the document.
 */
applyOperation(op: Operation): void {}

/**
 * Undoes the last operation that was applied to the document. If there
 * is no operation to undo, then do nothing.
 */
undoLast(): void {}

/**
 * Redoes the last operation that was undone to the document. If there
 * is no operation to redo, then do nothing.
 */
redoLast(): void {}

/**
 * Return the current content of the document as a string.
 */
getCurrentContent(): string {}
Below, we also have some test cases in Typescript to demonstrate the expected behavior.

const DEBUG_logCurrentContent = (doc: TextDocument) => {
    console.log(Current content is: ${doc.getCurrentContent()})
}

const doc = new TextDocument()
DEBUG_logCurrentContent(doc) // should print ""

doc.applyOperation({ type: "insertAtEnd", charsToInsert: "hello" })
DEBUG_logCurrentContent(doc) // should print "hello"

doc.applyOperation({ type: "insertAtEnd", charsToInsert: "world" })
DEBUG_logCurrentContent(doc) // should print "helloworld"

doc.applyOperation({ type: "deleteFromEnd", numCharsToDelete: 5 })
DEBUG_logCurrentContent(doc) // should print "hello"

doc.undoLast()
DEBUG_logCurrentContent(doc) // should print "helloworld"

doc.redoLast()
DEBUG_logCurrentContent(doc) // should print "hello"
"""

# OPTIMAL
"""
Insert/Delete: O(k), where k is the number of characters inserted or deleted
Undo/Redo: O(k), for reversing the previous operation
getCurrentContent: O(n), to join the list of characters
Space: O(n + u + r), where n is the current content length, u and r are the sizes of undo/redo stacks
"""

class TextDocument:
    def __init__(self):
        self.content = []  # Store content as a list of characters
        self.undo_stack = []  # Stores inverse operations for undo
        self.redo_stack = []  # Stores operations for redo

    def applyOperation(self, op: dict):
        op_type = op["type"]

        if op_type == "insertAtEnd":
            chars = op["charsToInsert"]
            self.content.extend(chars)
            self.undo_stack.append({
                "type": "deleteFromEnd",
                "numCharsToDelete": len(chars)
            })
            self.redo_stack.clear()

        elif op_type == "deleteFromEnd":
            n = op["numCharsToDelete"]
            actual_n = min(n, len(self.content))
            deleted = self.content[-actual_n:]
            self.content = self.content[:-actual_n]
            self.undo_stack.append({
                "type": "insertAtEnd",
                "charsToInsert": "".join(deleted)
            })
            self.redo_stack.clear()

    def undoLast(self):
        if not self.undo_stack:
            return
        inverse_op = self.undo_stack.pop()
        self._applyAndRecord(inverse_op, self.redo_stack)

    def redoLast(self):
        if not self.redo_stack:
            return
        inverse_op = self.redo_stack.pop()
        self._applyAndRecord(inverse_op, self.undo_stack)

    def _applyAndRecord(self, op: dict, record_stack: list):
        # Like applyOperation, but records inverse into record_stack
        op_type = op["type"]

        if op_type == "insertAtEnd":
            chars = op["charsToInsert"]
            self.content.extend(chars)
            record_stack.append({
                "type": "deleteFromEnd",
                "numCharsToDelete": len(chars)
            })

        elif op_type == "deleteFromEnd":
            n = op["numCharsToDelete"]
            actual_n = min(n, len(self.content))
            deleted = self.content[-actual_n:]
            self.content = self.content[:-actual_n]
            record_stack.append({
                "type": "insertAtEnd",
                "charsToInsert": "".join(deleted)
            })

    def getCurrentContent(self) -> str:
        return "".join(self.content)




# My solution 
class Operation:
    pass


class InsertAtEndOperation(Operation):
    def __init__(self, chars_to_insert: str):
        self.chars_to_insert = chars_to_insert

class DeleteFromEndOperation(Operation):
    def __init__(self, num_chars_to_delete: int):
        self.num_chars_to_delete = num_chars_to_delete

class TextDocument:
    def __init__(self) -> None:
        self.content = [] # for everything
        self.undo_st = []
        self.redo_st = []

    def apply_operation(self, op: Operation) -> None:
        if isinstance(op, InsertAtEndOperation):
            chars = op.chars_to_insert
            self.content.extend(chars)
            self.undo_st.append(DeleteFromEndOperation(len(chars)))
            self.redo_st.clear()
        if isinstance(op, DeleteFromEndOperation):
            n = op.num_chars_to_delete
            deleted = self.content[-n:] if n <= len(self.content) else self.content[:]
            self.content = self.content[:-n] if n <= len(self.content) else []
            self.undo_st.append(InsertAtEndOperation("".join(deleted)))
            self.undo_st.clear()

    def undo_last(self) -> None:
        if not self.undo_st:
            return 
        last_op = self.undo_st.pop()
        self._reverse_action(last_op, to_redo = True)
        

    def redo_last(self) -> None:
        if not self.redo_st:
            return 
        last_op = self.redo_st.pop()
        self._reverse_action(last_op, to_undo = True)

    def get_current_content(self) -> str:
        return "".join(self.content) 
        
    def _reverse_action(self, op: Operation, to_redo: bool = False, to_undo: bool = False):
        if isinstance(op, InsertAtEndOperation):
            self.content.extend(op.chars_to_insert)
            if to_redo:
                self.redo_st.append(DeleteFromEndOperation(len(op.chars_to_insert)))
            if to_undo:
                self.undo_st.append(DeleteFromEndOperation(len(op.chars_to_insert)))
        elif isinstance(op, DeleteFromEndOperation):
            n = op.num_chars_to_delete
            deleted = self.content[-n:] if n <= len(self.content) else self.content[:]
            self.content = self.content[:-n] if n <= len(self.content) else []
            inverse = InsertAtEndOperation("".join(deleted))
            if to_redo:
                self.redo_st.append(inverse)
            if to_undo:
                self.undo_st.append(inverse)
        
    
        
def test_simple_undo_redo():
    doc = TextDocument()
    assert doc.get_current_content() == ""

    doc.apply_operation(InsertAtEndOperation("hello"))
    assert doc.get_current_content() == "hello"

    
    doc.apply_operation(InsertAtEndOperation("world"))
    # print(doc.get_current_content())
    assert doc.get_current_content() == "helloworld"

    doc.apply_operation(DeleteFromEndOperation(5))
    assert doc.get_current_content() == "hello"

    doc.undo_last()
    print(doc.get_current_content())
    assert doc.get_current_content() == "helloworld"

    doc.redo_last()
    assert doc.get_current_content() == "hello"
    
    print("test_simple_undo_redo passes")

test_simple_undo_redo()
