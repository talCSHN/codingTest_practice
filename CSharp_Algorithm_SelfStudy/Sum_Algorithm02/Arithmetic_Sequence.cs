namespace Sum_Algorithm02
{
    internal class Arithmetic_Sequence
    {
        static void Main(string[] args)
        {
            // [1] Input
            var sum = 0;


            // [2] Process
            for (int i = 1; i <= 20; i++)
            {
                if (i % 2 != 0)
                {
                    sum += i;
                }
            }

            // [3] Output
            Console.WriteLine(sum);
        }
    }
}
