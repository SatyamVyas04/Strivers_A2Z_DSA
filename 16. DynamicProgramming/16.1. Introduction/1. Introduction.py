# ================================
# BASICS
# ================================
# Tabulation  -> Bottom-Up approach
# Memoization -> Top-Down approach

# ================================
# FLOW
# ================================
# 1. Start with Memoization (Top-Down) to optimize brute force recursion.
# 2. Convert to Tabulation (Bottom-Up) for a clean, iterative solution.
# 3. Optimize Space Complexity (SC) if possible for the final optimal solution.

# ================================
# INTUITION
# ================================
# 1. Identify overlapping subproblems that repeat during recursion.
# 2. Store results of these subproblems in a dp table (list/dict) -> Memoization.
# 3. When a subproblem repeats, reuse the stored result instead of recalculating.

# ================================
# COMPLETE FLOW
# ================================
# 1. Recursion  -> Write a basic recursive solution.
# 2. Base Case  -> Identify smallest inputs where the answer is known.
# 3. Memoization -> Store solutions to overlapping subproblems.
# 4. Tabulation -> Replace recursion with an iterative dp[] array or table.
# 5. Space Optimization -> Reduce dp storage to minimal variables when possible.
