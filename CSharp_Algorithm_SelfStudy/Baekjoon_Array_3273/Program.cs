﻿/*
문제
n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

출력
문제의 조건을 만족하는 쌍의 개수를 출력한다. 
*/
namespace Baekjoon_Array_3273
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] list = Console.ReadLine().Split();
            List<int> realList = new List<int>();
            foreach (string s in list)
            {
                realList.Add(int.Parse(s));
            }
            int x = int.Parse(Console.ReadLine());
            int resSum = 0;
            int start = 0;
            int end = n - 1;
            realList.Sort();
            while (start < end)
            {
                if (realList[start] + realList[end] == x)
                {
                    resSum++;
                    start++;
                    end--;
                }
                else if (realList[start] + realList[end] < x)
                {
                    start++;
                }
                else
                {
                    end--;
                }
            }
            
            Console.WriteLine(resSum);
           
        }
    }
}
