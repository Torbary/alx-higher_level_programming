#include <stdio.h>
#include "Python.h"

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/*
 * print_python_list - print info about a Python list obj
 * @p: a pyObject list object
 */


void print_python_list(PyObject *p)
{
	/*Declare vaiable to store size, allocated size and
	 * index of the list*/
	Py_ssize_t size, alloc, i;
	/*Declare variable to the type of an element in the list*/
	const char *type;
	/*cast the given obj pointer to a PyListObject pointer*/
	PyListObject *list = (PyListObject *)p;
	/*Cast the given object pointer to a PyVarObject pointer*/
	PyVarObject *var = (PyVarObject *)p;

	/*Assign the size of the list to the size variable*/
	size = var->ob_size;
	/*Assign the allocated size of the list to the allocated variable*/
	alloc = list->allocated;

	/*flush out the stdout buffer*/
	fflush(stdout);

	/*Print a message about the list*/
	printf("[*] Python list info\n");

	/*Check if the given object is a python list*/
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		/*If not, print an error message and return*/
		printf(" [ERROR] Invalid List Object\n");
		return;
	}

	/*Print the size of the list*/
	printf("[*] Size of the Python List = %ld\n", size);
	/*print the allocated size of the list*/
	printf("[*] Allocated = %ld\n", alloc);

	/*Loop through each element in the list*/
	for (i = 0; i < size; i++)
	{
		/*Assign the type of current element to the
		 * type variable*/
		type = list->ob_item[i]->ob_type->tp_name;
		/*Print the index and type of the current element*/
		printf("Element %ld: %s\n", i, type);
		/*If the element is of a byte type,
		 * call the print_python_byte funtion*/
		if (strcmp(type, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[i]);
		}
		/*Else if the element is of type float,
		 * call the print_python_float function
		 */
		else if (strcmp(type, "float") == 0)
		{
			print_python_float(list->ob_item[i]);
		}
	}

}



/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 * how does it works?:
 * This is a C function that takes a pointer to a Python object
 * as an argument and prints information about it.
 * It first checks if the object is a Python bytes object, and if not,
 * it prints an error message and returns.
 * If it is a bytes object, it then prints the size of the bytes object,
 * the string representation of the bytes object
 * and the first 10 bytes of the bytes object in hexadecimal format,
 * if the size of the bytes object is greater than 10. 
 * if not it will print the available bytes.
 */


void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	/*Check if the given object is a Python bytes object*/
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	
	/*Check if the size of the bytes object is greater than or
	 * equal to 10*/
	if (((PyVarObject *)p)->ob_size >= 10)
		/*if so set size to 10*/
		size = 10;
	else
		/* Else, set the size variable to the size
		 * of the bytes object + 1*/
		size = ((PyVarObject *)p)->ob_size + 1;

	/*Print the number of bytes to be printed*/
	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		/*Print the current byte in hexadecimal format*/
		printf("%02hhx", bytes->ob_sval[i]);
		/*Check if this is the last byte*/
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");

	}
}





/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 * This is a C function that takes a pointer to a Python object as an argument
 * and prints information about it. 
 * It first checks if the object is a Python float object, 
 * and if not, it prints an error message and returns. 
 * If it is a float object, it then converts the float object
 * to a string representation using the PyOS_double_to_string function,
 * prints the string representation and then frees the buffer.
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;
	/*Cast the given object pointer to a PyFloatObject pointer*/

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	/*convert the float object to a string representation
	 * using the PyOS_double_to_string function*/

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}



















