# Python Data Structures Lab

Hands-on practice with Python's four built-in data structures: **list**, **tuple**, **set**, and **dict**.
You will finish by building a brute-force login detector from a real-looking SSH log.

Everything runs in **GitHub Codespaces**, in your web browser. You do not need to install anything.

## The labs

| Lab | Folder | Topic | Time |
|-----|--------|-------|------|
| 1 | `lab1_lists_tuples/` | Lists and tuples (warm-up) | about 20 min |
| 2 | `lab2_sets_dicts/` | Sets and dictionaries | about 25 min |
| 3 | `lab3_speed/` | **OPTIONAL:** Make it faster (list vs. set) | about 15 min |
| 4 | `lab4_capstone/` | Capstone: brute-force login detector | about 40 min |

Lab 3 is optional. If you are short on time, skip it and go straight to Lab 4.

## Steps

### 1. Get your own copy

At the top of this page, click **Use this template**, then **Create a new repository**.
(You can also click **Fork**.) Put the copy in **your own** GitHub account.

### 2. Open a Codespace

1. Go to **your copy** of the repository (check that your username is at the top left).
2. Click the green **Code** button.
3. Click the **Codespaces** tab.
4. Click **Create codespace on main**.
5. Wait. VS Code will load in your browser. The first time can take a minute or two.

> **No token needed.** Inside a Codespace, GitHub signs you in automatically.
> You do **not** need a Personal Access Token like in the morning Git class.
> `git push` just works.

### 3. Make your branch

Open the terminal at the bottom of VS Code. (If you do not see it, use the menu: **Terminal → New Terminal**.)
Type this, using your own name instead of `YOURNAME`:

```
git checkout -b YOURNAME-python
```

### 4. Do each lab

Repeat these steps for Lab 1, Lab 2, (Lab 3 if you want), then Lab 4.

1. Open the lab file, for example `lab1_lists_tuples/lab1.py`.
2. Read the comments. Each task has a `# TODO` comment that tells you what to do
   and what the answer should be.
3. Replace each `None` with your answer.
4. Run the file in the terminal:

   ```
   python lab1_lists_tuples/lab1.py
   ```

   The checker at the bottom of the file runs automatically.
   It shows `PASS` or `FAIL` for each task. A `FAIL` comes with a hint.
5. Keep editing and re-running until every task passes.
6. Save your work to GitHub:

   ```
   git add .
   git commit -m "Finished lab 1"
   git push
   ```

   **First push only:** `git push` will complain that your branch has no upstream.
   Use this instead, one time:

   ```
   git push -u origin YOURNAME-python
   ```

   After that, plain `git push` works.

The commands to run each lab:

```
python lab1_lists_tuples/lab1.py
python lab2_sets_dicts/lab2.py
python lab3_speed/lab3.py
python lab4_capstone/lab4.py
```

### 5. Open a pull request

When you are done with the labs:

1. Go to **your copy** of the repository on GitHub.
2. Click **Pull requests**, then **New pull request**.
3. Set **base** to `main` and **compare** to `YOURNAME-python`.
4. Click **Create pull request**. Give it a short title, like "Python labs: YOURNAME".

### 6. Stop your Codespace

When you are finished, stop the Codespace so it does not use up your free hours:
click **Codespaces** in the bottom-left corner of VS Code, then **Stop Current Codespace**.
(Or go to [github.com/codespaces](https://github.com/codespaces), click the `...` next to your Codespace, and click **Stop codespace**.)

## Important

**Do not edit anything below the `CHECKER: DO NOT EDIT BELOW THIS LINE` banner** in each lab file.
You are welcome to *read* the checker code. It is real Python and a good example. Just don't change it.

## Stuck?

1. Re-read the `# TODO` comment. It tells you which tool to use and what the answer should be.
2. Read the hint on the `FAIL` line. It points you toward the fix.
3. Seeing red text that starts with `Traceback` instead of PASS/FAIL? Your code stopped
   before the checker could run. Read the **last line** of the red text. It names the problem,
   for example `KeyError: '22'` (that key is not in the dictionary) or
   `IndexError: list index out of range` (no item at that index). The line number just above it
   shows where. Fix that line and run the file again.
4. Ask an instructor. That is what we are here for.
