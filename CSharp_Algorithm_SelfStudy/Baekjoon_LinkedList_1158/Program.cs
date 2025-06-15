using System.Text;

namespace Baekjoon_LinkedList_1158
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] inputs = Console.ReadLine().Split();
            int[] realInputs = new int[2];
            LinkedList<int> people = new LinkedList<int>();
            List<int> answer = new List<int>();
            
            for (int k = 0; k < 2; k++)
            {
                realInputs[k] = int.Parse(inputs[k]);
            }
            
            for (int i = 1; i <= realInputs[0]; i++)
            {
                people.AddLast(i);
            }
            
            var cursor = people.First;

            while (people.Count > 0)
            {
                for (int i = 0; i < realInputs[1] - 1; i++)
                {
                    cursor = (cursor.Next != null) ? cursor.Next : people.First;
                }
                answer.Add(cursor.Value);
                var next = (cursor.Next != null) ? cursor.Next : people.First;
                people.Remove(cursor);
                cursor = (people.Count > 0) ? next : null;
                
            }

            Console.WriteLine("<" + string.Join(", ", answer) + ">");
        }
    }
}
