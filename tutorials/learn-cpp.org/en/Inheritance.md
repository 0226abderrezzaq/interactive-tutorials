Tutorial
--------

Let's extend the `class Point` from the previous tutorial to handle Complex numbers. The real and imaginary numbers will be defined as private integer references to coordinates of the Point object. 

    #include <iostream>
    using namespace std;

    template<typename T>
    void Swap(T &a, T &b) { T temp = a; a = b; b = temp; }
  
    class Point {
    public:
        int x, y;

        Point (int c1, int c2) { x = c1; y = c2;}
        Point& operator=(Point rhs) {
            x = rhs.x; y = rhs.y;
            return *this;
        }
    };
    
    class Complex : public Point {
      private: 
        int &real, &imag;
      public: 
        Complex(int r, int i) : Public (r, i), real (x), imag (y) 
        { cout << "Forming..." << *this; }
        
    };
    
    
    int main()
    {

        Complex c1(15, 15), c2 (100, 100); 
        return 0;
    }

    std::ostream& operator<<(std::ostream& out, const Point& c)
    {
      out<< "x:" << c.x << " ";
      out<< "y:" << c.y << "\n";
      return out;
    }
    
### Inheritance and Friends

Exercise
--------
The Swap function will also work with user-defined data types. To demonstrate this, implement a C++ `class Point` which has coordinates x and y. 
Operator overloading for the operator `=` also has to be implemented. 

Tutorial Code
-------------

    #include <iostream>
    using namespace std;
    
    class Point;
    std::ostream& operator<<(std::ostream& out, const Point& c);
    
    template<typename T>
    void Swap(T &a, T&b)
    {
        T temp = a;
        a = b;
        b = temp; 
    }
    
    class Point
    {
        // Your code goes here
         
        Point& operator=(Point rhs)
        {
            // your code goes here
     
        }
    };
    
    int main() {
    
        Point p1(5,5), p2(100, 100);
        Swap (p1, p2);
      
        cout << p1 << p2 << std::endl;
        return 0;
    }
    
    std::ostream& operator<<(std::ostream& out, const Point& c)
    {
       out<< "x:" << c.x << " ";
       out<< "y:" << c.y << "\n";
       return out;
    }

Expected Output
---------------

    p1: x:100 y:100
    p2: x:5 y:5

Solution
--------

    #include <iostream>
    using namespace std;

    class Point;
    std::ostream& operator<<(std::ostream& out, const Point& c);

    template<typename T>
    void Swap(T & a, T & b) //"&" passes parameters by reference
    {
      T temp = b;
      b = a;
      a = temp;
    }

    class Point {
    public:
        int x, y;

        Point (int c1, int c2) { x = c1; y = c2;}
        Point& operator=(Point rhs) {
            x = rhs.x; y = rhs.y;
            return *this;
        }
    };

    int main()
    {

        Point p1(5,5), p2 (100,100);
        Swap (p1, p2);
        cout << "p1: " << p1 << "p2: " << p2 << endl;
        return 0;
    }

    std::ostream& operator<<(std::ostream& out, const Point& c)
    {
      out<< "x:" << c.x << " ";
      out<< "y:" << c.y << "\n";
      return out;
    }
