I-Logix-RPY-Archive version 8.14.0 C++ 9810313
{ IProject 
	- _id = GUID 19f628d6-269c-4a33-9a31-15df12f70b38;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 4;
			- value = 
			{ IPropertySubject 
				- _Name = "CPP_Roundtrip";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "General";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "RoundtripScheme";
								- _Value = "Basic";
								- _Type = Enum;
								- _ExtraTypeInfo = "Respect,Advanced,Basic";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "Format";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Transition";
						- Properties = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IProperty 
								- _Name = "Font.Font";
								- _Value = "Tahoma";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Font.FontColor";
								- _Value = "0,0,0";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Font.Size";
								- _Value = "8";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "128,128,128";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineWidth";
								- _Value = "1";
								- _Type = Int;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "General";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Model";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ModelCodeAssociativityFineTune";
								- _Value = "Bidirectional";
								- _Type = Enum;
								- _ExtraTypeInfo = "Bidirectional,RoundTrip,CodeGeneration,Never";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "StatechartDiagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Transition";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
							{ IProperty 
								- _Name = "line_style";
								- _Value = "rectilinear_arrows";
								- _Type = Enum;
								- _ExtraTypeInfo = "straight_arrows,rectilinear_arrows,spline_arrows,rounded_rectilinear_arrows";
							}
						}
					}
				}
			}
		}
	}
	- _name = "IoT-Device";
	- _modifiedTimeWeak = 6.27.2017::7:28:5;
	- _lastID = 4;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _name = "Test";
		- _id = GUID f5881f2d-654d-4234-93fa-810af18a4fb6;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _subsystem = "Test";
		- _name = "Test";
		- _id = GUID 6323eb2e-c116-412d-8542-44ca0c41c865;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 3;
		- value = 
		{ ISubsystem 
			- fileName = "Test";
			- _id = GUID f5881f2d-654d-4234-93fa-810af18a4fb6;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre821Cpp";
			- _id = GUID 00b0140e-6d06-4d19-ba99-8a8e40131db7;
		}
		{ ISubsystem 
			- fileName = "IOT_DEVICE";
			- _id = GUID b745dc08-3c72-4092-8081-d8839dbdb41a;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 0;
	}
	- Components = { IRPYRawContainer 
		- size = 0;
	}
}

