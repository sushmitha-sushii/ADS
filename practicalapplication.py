class WordSearch:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def dfs(self, word, i, j, index):
        if index == len(word):
            return True
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or self.grid[i][j] != word[index]:
            return False
        temp = self.grid[i][j]
        self.grid[i][j] = '#'

        found = (self.dfs(word, i+1, j, index+1) or  
                 self.dfs(word, i-1, j, index+1) or  
                 self.dfs(word, i, j+1, index+1) or  
                 self.dfs(word, i, j-1, index+1))    
        
        self.grid[i][j] = temp
        return found
    
    def exists(self, word):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == word[0] and self.dfs(word, i, j, 0):
                    return True
        return False

grid = [
    ['A', 'B', 'C', 'E'],
    ['S', 'U', 'I', 'J'],
    ['H', 'D', 'L', 'G']
]

word_search = WordSearch(grid)

word =input("Enter a word: ")

if word_search.exists(word):
    print(f"The word '{word}' exists in the grid.")
else:
    print(f"The word '{word}' does not exist in the grid.")
