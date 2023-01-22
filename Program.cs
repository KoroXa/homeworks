double A, B;
A = double.Parse(Console.ReadLine());
string C = Console.ReadLine();
B = double.Parse(Console.ReadLine());

if (C == "+")
{
    Console.WriteLine(A + B);
}
if (C == "-")
{
    Console.WriteLine(A - B);
}
if (C == "/")
{
    Console.WriteLine(A / B);
}
if (C == "*")
{
    Console.WriteLine(A * B);
}