// n명의 국어 점수 중에서 80점 이상인 점수의 합계
namespace Sum_Algorithm.Algorithms
{
    internal class Sum_Algorithm
    {
        static void Main(string[] args)
        {
            // [1] Input : n명의 국어 점수
            //int[] scores = { 100, 75, 50, 37, 90, 95};
            List<int> scores = new List<int> { 100, 75, 50, 37, 90, 95 };
            int sum = 0;
            //[2] Process
            //for (int i = 0; i < scores.Count; i++)
            //{
            //    if (scores[i] >= 80)
            //    {
            //        sum += scores[i];
            //    }
            //}
            sum = scores.Where(x => x >= 80).Sum();

            // [3] Output
            Console.WriteLine($"{scores.Count}명의 점수 중 80점 이상의 총점: {sum}");
        }
    }
}
