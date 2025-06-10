namespace Average_Algorithm
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // string[] answer = strings.OrderBy(s => s[n]).ThenBy(s => s).ToArray();
            int n = 1;
            string temp = null;
            string[] strings = new string[] { "cnbc", "anbcd" };
            for (int i = 0; i < strings.Length - 1; i++)
            {
                for (int j = i + 1; j < strings.Length; j++)
                {
                    if (strings[i][n] > strings[j][n])
                    {
                        temp = strings[i];
                        strings[i] = strings[j];
                        strings[j] = temp;
                    }
                    else if (strings[i][n] == strings[j][n])
                    {
                        if (strings[i].CompareTo(strings[j]) == 1)
                        {
                            temp = strings[i];
                            strings[i] = strings[j];
                            strings[j] = temp;
                        }
                    }
                }
            }

        }
    }
}
