// 1부터 1000까지의 정수 중 13의 배수의 개수
namespace Count_Algorithm
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // 1. Input
            var numbers = Enumerable.Range(1, 1_000).ToList();
            int countNum = 0;
            // 2. Process
            countNum = numbers.Where(n => n % 13 == 0).Count(); 

            // 3. Output
            Console.WriteLine(countNum);
        }
    }
}
