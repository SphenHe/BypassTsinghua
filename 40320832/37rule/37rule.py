#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
This is a module for the problem 37 (Best Applicant)

This module reads two integers n and k from the input, and then
prints the number of ways to select k applicants from n applicants.

'''


# Generate all permutation of a given list
def generate_permutation(nums: list) -> list:
    '''
    Generate all permutation of a given list

    ### Input:
        - nums: list of numbers

    ### Output:
        - list of all permutation of the given list
    '''
    if len(nums) == 1:
        return [nums]
    else:
        result = []
        for i, num in enumerate(nums):
            rest = nums[:i] + nums[i + 1:]
            for j in generate_permutation(rest):
                result.append([num] + j)
        return result

# Check if I can get the best applicant
def isBestApplicant(applicants: list, n:int, k: int) -> bool:
    '''
    Check if I can get the best applicant

    ### Input:
        - applicants: list of applicants
        - n: the best applicant
        - k: the number of applicants to interview

    ### Output:
        - True if I can get the best applicant, False otherwise
    '''
    bestK = 0
    for i in applicants[:k]: # best of the first k applicants
        if i == n:
            return False
        else:
            bestK = max(bestK, i)
    for i in applicants[k:]: # select the first one better than the best
        if i > bestK:
            return i == n
    return False

def main():
    '''
    The main function to run the program, which reads two integers n and k from the input,
    and then prints the number of ways to select k applicants from n applicants.

    ### Input:
        - n: the number of applicants
        - k: the number of applicants to interview

    ### Output:
        - the number of ways to select k applicants from n applicants
    '''
    # read n and k
    n = int(input())
    k = int(input())

    bestApplicantSelectedCounter = 0

    for applicants in generate_permutation(list(range(1, n + 1))):
        if isBestApplicant(applicants, n, k):
            bestApplicantSelectedCounter += 1

    print(bestApplicantSelectedCounter)

if __name__ == '__main__':
    main()
