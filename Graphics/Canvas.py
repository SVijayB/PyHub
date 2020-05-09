from tkinter import *
def doc():
    """
Using the Tkinter canvas :
• bd                        : Border Width in pixels. Default value : 2
• bg                        : Background Colour.
• Confine                   : If true, the canvas cannot be scrolled outside the scroll region.
• Cursor                    : The cursor is used in the canvas like an arrow, circle or a dot.
• Height                    : Used to set the size of the canvas in the Y-dimension.
• Highlightcolor            : Changes the highlight colour.
• Relief                    : Type of border - Raised, ridge, groove, sharpened. 
• Scrollregion              : It is a tuple that defines over how large in area the canvas can be scrolled.
                              It takes values in the west,north,east and south(Exact order).
• Width                     : Used to set the size of the canvas in the X-dimension.
• xscrollincrement          : If set in +ve number, then canvas can only be placed in multiples of that number.
• xscrollcommand            : Canvas scrolling in the horizontal direction.
• yscrollincrement          : Similar to the xscrollincrement
• yscrollcommand            : Similar to the xscrollcommand but in vertical direction.
Some Standards : 
    • Arc
    • Image
    • Line
    • Oval
    • Polygon
    """
print(doc.__doc__)
