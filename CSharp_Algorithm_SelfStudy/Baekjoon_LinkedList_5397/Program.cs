using System.Collections;

namespace Baekjoon_LinkedList_5397
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int tcNum = int.Parse(Console.ReadLine());
            List<string> list = new List<string>();
            for (int k = 0; k < tcNum; k++)
            {
                string testCase = Console.ReadLine();
                list.Add(testCase);
            }
            //List<char> tmpList = new List<char>();
            //ArrayList tmpList = new ArrayList();
            //string tmpList = string.Empty;
            //foreach (string tc in list)
            //{
            //    list.Add(tc);
            //}
            for (int i = 0; i < tcNum; i++)
            {
                //char?[] tmpList = new char?[list[i].Length];
                List<char> tmpList = new List<char>(list[i].Length);
                int pos = 0;
                foreach (char c in list[i])
                {
                    if (c == '<')
                    {
                        if (pos > 0)
                        {
                            pos -= 1;
                        }
                        else
                        {
                            pos = 0;
                        }
                    }
                    else if (c == '>')
                    {
                        if (pos < tmpList.Count)
                        {
                            pos += 1;
                        }
                    }
                    else if (c == '-')
                    {
                        if (pos != 0)
                        {
                            //tmpList[--pos] = null;
                            tmpList.RemoveAt(--pos);
                        }
                    }
                    else
                    {
                        //tmpList[pos] = c;
                        tmpList.Insert(pos, c);
                        pos++;
                    }
                }
                tmpList.ForEach(c => Console.Write(c));
                tmpList.Clear();
                Console.WriteLine();
            }
        }
    }
}
