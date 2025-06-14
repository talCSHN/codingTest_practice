using System.Collections;
using System.Text;

namespace Baekjoon_LinkedList_5397
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int tcNum = int.Parse(Console.ReadLine());
            List<string> tc = new List<string>();
            for (int j = 0; j < tcNum; j++)
            {
                string temp = Console.ReadLine();
                tc.Add(temp);
            }
            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < tcNum; i++)
            {
                string testCase = tc[i];
                //List<char> password = new List<char>(testCase.Length);
                Stack<char> left = new Stack<char>();
                Stack<char> right = new Stack<char>();
                //var cursor = 0;
                foreach (char c in testCase)
                {
                    if (c == '<')
                    {
                        if (left.Count > 0)
                        {
                            right.Push(left.Pop());
                        }

                    }
                    else if (c == '>')
                    {
                        if (right.Count > 0)
                        {
                            left.Push(right.Pop());
                        }
                    }
                    else if (c == '-')
                    {
                        if (left.Count > 0)
                        {
                            left.Pop();
                        }
                    }
                    else
                    {
                        left.Push(c);
                    }
                }
                while (left.Count > 0)
                {
                    right.Push(left.Pop());
                }
                while (right.Count > 0)
                {
                    sb.Append(right.Pop());
                }
                sb.Append("\n");
                
            }
            Console.WriteLine(sb.ToString());

        }
    }
}
