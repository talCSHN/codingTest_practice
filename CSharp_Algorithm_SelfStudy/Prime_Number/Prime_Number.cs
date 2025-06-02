// 특정 수를 입력 받아서, 소수 여부 판별
namespace Prime_Number
{
    internal class Prime_Number
    {
        static void Main(string[] args)
        {
            // Input
            var number = 0;
            Console.Write("수 입력 : _\b");
            number = Convert.ToInt32(Console.ReadLine());
            // Process
            var i = 1;
            do
            {
                i = i + 1;  // 2부터 n까지 비교
            }
            while (number % i != 0);

            // Output
            if (number == i)
            {
                Console.WriteLine("소수");
            }
            else
            {
                Console.WriteLine("소수 아님");
            }
        }
    }
}
