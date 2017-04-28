# !/user/lib/python
"""
tableprint.py
"""
import cStringIO
import operator
#  Code taken from
#  http://code.activestate.com/recipes/267662-table-indentation/


def indent(rows_list, has_header=False, header_char='-', delimit=' | ', justify='left',
           separate_rows=False, prefix='', postfix='', wrapfunc=lambda x: x):
    """
        Indents a table by column.
       - rows: A sequence of sequences of items, one sequence per row.
       - has_header: True if the first row consists of the columns' names.
       - header_char: Character to be used for the row separator line
         (if hasHeader==True or separateRows==True).
       - delimit: The column delimiter.
       - justify: Determines how are data justified in their column.
         Valid values are 'left', 'right' and 'center'.
       - separate_rows: True if rows are to be separated by a line
         of 'headerChar's.
       - prefix: A string prepended to each printed row.
       - postfix: A string appended to each printed row.
       - wrapfunc: A function f(text) for wrapping text; each element in
         the table is first wrapped by this function.
    """
    #  closure for breaking logical rows to physical, using wrapfunc
    def row_wrapper(row_):
        new_rows = [wrapfunc(item_).split('\n') for item_ in row_]
        return [[substr or '' for substr in item_] for item_ in map(None, *new_rows)]
    #  break each logical row into one or more physical ones
    logical_rows = [row_wrapper(row_value) for row_value in rows_list]
    #  columns of physical rows
    columns = map(None, *reduce(operator.add, logical_rows))
    #  get the maximum of each column by the string length of its items
    max_widths = [max([len(str(item)) for item in column]) for column in columns]
    row_separator = header_char * (len(prefix) + len(postfix) + sum(max_widths) +
                                   len(delimit)*(len(max_widths)-1))
    #  select the appropriate justify method
    justify = {'center':str.center, 'right':str.rjust, 'left':str.ljust}[justify.lower()]
    output = cStringIO.StringIO()
    if separate_rows: print >> output, row_separator
    for physical_rows in logical_rows:
        for row1 in physical_rows:
            print >> output, \
                prefix \
                + delimit.join([justify(str(item), width_value) for (item, width_value) in zip(row1, max_widths)]) \
                + postfix
        #  SNAPROUTE change, don't want to seperate rows for help display
        if has_header: print >> output, row_separator; has_header = False
    return output.getvalue()

#  written by Mike Brown
#  http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/148061


def wrap_onspace(text, width_value):
    """
    A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\n).
    """
    return reduce(lambda line, word, width_=width_value: '%s%s%s' %
                  (line,
                   ' \n'[(len(line[line.rfind('\n')+1:])
                          + len(word.split('\n', 1)[0]
                              ) >= width_value)],
                   word),
                  text.split(' ')
                 )


import re
def wrap_onspace_strict(text, width_value):
    """
    Similar to wrap_onspace, but enforces the width constraint:
    words longer than width are split.
    """
    word_regex = re.compile(r'\S{'+str(width_value)+r', }')
    return wrap_onspace(word_regex.sub(lambda m: wrap_always(m.group(), width_value), text), width_value)


import math
def wrap_always(text, width_value):
    """
    A simple word-wrap function that wraps text on exactly width characters.
    It doesn't split the text in words.
    """
    return '\n'.join([text[width_value*i:width_value*(i+1)] \
                      for i in xrange(int(math.ceil(1.*len(text)/width_value)))])


if __name__ == '__main__':
    labels = ('First Name', 'Last Name', 'Age', 'Position')
    data = \
    '''John, Smith, 24, Software Engineer
       Mary, Brohowski, 23, Sales Manager
       Aristidis, Papageorgopoulos, 28, Senior Reseacher'''
    rows = [row.strip().split(',')  for row in data.splitlines()]

    print 'Without wrapping function\n'
    print indent([labels]+rows, has_header=True)
    #  test indent with different wrapping functions
    width = 10
    for wrapper in (wrap_always, wrap_onspace, wrap_onspace_strict):
        print 'Wrapping function: %s(x, width=%d)\n' % (wrapper.__name__, width)
        print indent([labels]+rows, has_header=True, separate_rows=True,
                     prefix='| ', postfix=' |',
                     wrapfunc=lambda x: wrapper(x, width))

    #  output:
    #
    # Without wrapping function
    #
    # First Name | Last Name        | Age | Position
    # -------------------------------------------------------
    # John       | Smith            | 24  | Software Engineer
    # Mary       | Brohowski        | 23  | Sales Manager
    # Aristidis  | Papageorgopoulos | 28  | Senior Reseacher
    #
    # Wrapping function: wrap_always(x, width=10)
    #
    # ----------------------------------------------
    # | First Name | Last Name  | Age | Position   |
    # ----------------------------------------------
    # | John       | Smith      | 24  | Software E |
    # |            |            |     | ngineer    |
    # ----------------------------------------------
    # | Mary       | Brohowski  | 23  | Sales Mana |
    # |            |            |     | ger        |
    # ----------------------------------------------
    # | Aristidis  | Papageorgo | 28  | Senior Res |
    # |            | poulos     |     | eacher     |
    # ----------------------------------------------
    #
    # Wrapping function: wrap_onspace(x, width=10)
    #
    # ---------------------------------------------------
    # | First Name | Last Name        | Age | Position  |
    # ---------------------------------------------------
    # | John       | Smith            | 24  | Software  |
    # |            |                  |     | Engineer  |
    # ---------------------------------------------------
    # | Mary       | Brohowski        | 23  | Sales     |
    # |            |                  |     | Manager   |
    # ---------------------------------------------------
    # | Aristidis  | Papageorgopoulos | 28  | Senior    |
    # |            |                  |     | Reseacher |
    # ---------------------------------------------------
    #
    # Wrapping function: wrap_onspace_strict(x, width=10)
    #
    # ---------------------------------------------
    # | First Name | Last Name  | Age | Position  |
    # ---------------------------------------------
    # | John       | Smith      | 24  | Software  |
    # |            |            |     | Engineer  |
    # ---------------------------------------------
    # | Mary       | Brohowski  | 23  | Sales     |
    # |            |            |     | Manager   |
    # ---------------------------------------------
    # | Aristidis  | Papageorgo | 28  | Senior    |
    # |            | poulos     |     | Reseacher |
    # ---------------------------------------------
