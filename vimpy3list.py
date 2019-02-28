python3 << endpy
import vim

def listPiP(listName, i= -1, scorpe = 'g'):
    """Pop item at index i from var listName of scope inserts item text"""

    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    item = workingList.pop(i)
    _listSet(workingList, listName, scope)
    vim.command('norm i{}'.format(str(item)))


def listPop(listName, i= -1, scope = 'g'):
    """Pop item at index i from var listName of scope"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    workingList.pop(i)
    _listSet(workingList, listName, scope)

def listAppend(x, listName, scope = 'g'):
    """Append x to var listName of scope"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    workingList.append(x)
    _listSet(workingList, listName, scope)

def listExtend(x, listName, scope = 'g'):
    """Extend x to var listName of scope"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    workingList.extend(x)
    _listSet(workingList, listName, scope)

def listInsert(i, x, listName, scope = 'g'):
    """Insert x at var listName[i] of scope"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    workingList.insert(i, x)
    _listSet(workingList, listName, scope)

def listIndex(x, listName, scope = 'g'):
    """Index of x from var listname of scope"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    index = workingList.index(x)
    print(index)

def listClear(listName, scope = 'g'):
    """Clear listName of scope"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    workingList = []
    _listSet(workingList, listName, scope)

def listClear(listName, newListName, scope = 'g', newScope = 'g'):
    """Copy listName of scope to newListName of newScope"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    workingList = []
    _listSet(workingList, listName, scope)

def listCount(x, listName, scope = 'g'):
    """Count the number of occurrences of x in listName of scope"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    count = workingList.count(x)
    print(count)

def listRemove(x, listName, scope = 'g'):
    """Remove x from var listname of scope"""
    workinglist = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    try:
        workingList.remove(x)
    except ValueError as e:
        print(e)
        return
    _listSet(workingList, listName, scope)

def listReverse(listName, scope = 'g'):
    """Reverse var listName of scope"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    workingList.reverse()
    _listSet(workingList, listName, scope)
    
def listSort(listName, R=False, scope = 'g'):
    """Sort var listName of scope R=True to reverse"""
    workingList = _listCheck(listName, scope)
    if len(workingList) != 0 and not workingList:
        return
    try:
        workingList.sort(reverse=R)
    except TypeError as e:
        print(e)
        return
    _listSet(workingList, listName, scope)

def _listCheck(listName, scope = 'g'):

    # If a list by the name listName doesn't exist, create one
    try:
        # Vars are accessed like this
        if scope == 'g':
            varType = type(vim.vars[listName]) 
            if varType == vim.List:
                workingList = list(vim.vars[listName])
            else:
                print('Variable {} in scope {} has type {}'.format(listName,
                      scope, varType))
                return
        elif scope == 'w':
            varType = type(vim.current.window.vars[listName]) 
            if type(vim.current.window.vars[listName]) == vim.List:
                workingList = list(vim.current.window.vars[listName])
            else:
                print('Variable {} in scope {} has type {}'.format(listName,
                      scope, varType))
                return
        elif scope == 'b':
            varType = type(vim.current.buffer.vars[listName]) 
            if type(vim.current.buffer.vars[listName]) == vim.List:
                workingList = list(vim.current.buffer.vars[listName])
            else:
                print('Variable {} in scope {} has type {}'.format(listName,
                      scope, varType))
                return
        elif scope == 't':
            varType = type(vim.current.tabpage.vars[listName]) 
            if type(vim.current.tabpage.vars[listName]) == vim.List:
                workingList = list(vim.current.tabpage.vars[listName])
            else:
                print('Variable {} in scope {} has type {}'.format(listName,
                      scope, varType))
                return
        else:
            print('Scope {} not found, please use g,w,t, or b instead.'.format(scope))
            return

    except KeyError:
        workingList = []
    return workingList

def _listSet(workingList, listName, scope = 'g'):
    if scope == 'g':
        vim.vars[listName] = workingList
    elif scope == 'w':
        vim.current.window.vars[listName] = workingList
    elif scope == 'b':
        vim.current.buffer.vars[listName] = workingList
    elif scope == 't':
        vim.current.tabpage.vars[listName] = workingList

endpy

