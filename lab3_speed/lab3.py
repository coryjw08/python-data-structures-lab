# =============================================================
#  LAB 3 (OPTIONAL): Make It Faster (about 15 minutes)
# =============================================================
#
#  THIS LAB IS OPTIONAL. If you are short on time, skip to Lab 4.
#
#  The story: you have a log with about 100,000 IP addresses, and a
#  threat-intel feed with about 7,000 known-bad IPs. You want to know how
#  many log entries came from a known-bad IP.
#
#  The code below already WORKS. It is just SLOW.
#  Your job is to change ONE line to make it fast.
#
#  How to work:
#    1. Run this file ONCE without changing anything:
#           python lab3_speed/lab3.py
#       It will take several seconds. Write down the time it prints.
#    2. Do TODO 1 below.
#    3. Run it again and compare the two times.
# =============================================================

# These two lines load tools that come with Python. You do not need to
# know how they work yet. "time" gives us a stopwatch. "Path" helps us
# find files.
import time
from pathlib import Path

# Find the data folder next to this lab, no matter where you run it from.
DATA_FOLDER = Path(__file__).parent.parent / "data"
LOG_FILE = DATA_FOLDER / "log_ips.txt"
THREAT_FILE = DATA_FOLDER / "threat_intel.txt"

# Read the log into a list of strings, one IP per line.
log_ips = open(LOG_FILE).read().splitlines()


# TODO 1: Make this line build a SET instead of a LIST.
#         Wrap the right-hand side in set( ... ).
#
#         Why is that faster? The loop below asks "is ip in bad_ips?"
#         100,000 times. With a LIST, Python checks the items one by one
#         until it finds a match, so each check is O(n). With a SET, Python
#         uses the hash of the IP to jump straight to it, so each check is O(1).
#
#         Expected: the same match count as before, in a tiny fraction of the time.
bad_ips = open(THREAT_FILE).read().splitlines()


# ----- Count the matches (do not change this part) -----
print(f"Checking {len(log_ips):,} log IPs against {len(bad_ips):,} threat-intel IPs...")
print(f"bad_ips is a {type(bad_ips).__name__}. Please wait...")

# perf_counter() is a stopwatch: read it before and after, then subtract.
start = time.perf_counter()

matches = 0
for ip in log_ips:
    if ip in bad_ips:
        matches = matches + 1

seconds = time.perf_counter() - start

print(f"Matches found: {matches}")
print(f"Time taken:    {seconds:.4f} seconds")
print()


# =============================================================
#  CHECKER: DO NOT EDIT BELOW THIS LINE
#  Run this file to check your work: python lab3.py
# =============================================================
#
#  Curious how the checker works? Read on. The check_task_...
#  function looks at your work and prints PASS or FAIL.
#  "try" / "except" catches errors so the checker never crashes.

LAB_NUMBER = 3


def report(number, name, passed, hint=""):
    """Print one PASS/FAIL line and return True or False."""
    if passed:
        print(f"PASS  Task {number}: {name}")
    else:
        print(f"FAIL  Task {number}: {name} ({hint})")
    return passed


def count_expected_matches():
    """Count the matches a second, independent way so we can compare."""
    threat_set = set(open(THREAT_FILE).read().splitlines())
    count = 0
    for log_ip in open(LOG_FILE).read().splitlines():
        if log_ip in threat_set:
            count = count + 1
    return count


def check_task_1_bad_ips_set():
    try:
        expected = count_expected_matches()
        if type(bad_ips) is not set:
            return report(1, "bad_ips is a set", False,
                          f"bad_ips is a {type(bad_ips).__name__}, not a set. "
                          "Wrap the right-hand side of that line in set( ... )")
        if matches != expected:
            return report(1, "bad_ips is a set", False,
                          f"bad_ips is a set, but the match count changed to {matches} "
                          f"(it should stay {expected}). Keep the original "
                          "open(THREAT_FILE).read().splitlines() exactly as it was, "
                          "and only wrap it in set( ... )")
        return report(1, "bad_ips is a set", True)
    except Exception as error:
        return report(1, "bad_ips is a set", False, f"checker error: {error}")


def run_checks():
    print("=" * 50)
    print(f"Checking Lab {LAB_NUMBER}...")
    print("=" * 50)
    results = [
        check_task_1_bad_ips_set(),
    ]
    passed = results.count(True)
    print("-" * 50)
    print(f"{passed}/{len(results)} tasks passing")
    if passed == len(results):
        print(f"Your loop took {seconds:.4f} seconds. Compare that with your first run!")
        print()
        print(f"Lab {LAB_NUMBER} complete: commit and push your work.")
        print("    git add .")
        print(f'    git commit -m "Finished lab {LAB_NUMBER}"')
        print("    git push")
    else:
        print("Read the FAIL hint above, fix it, and run this file again.")


run_checks()
