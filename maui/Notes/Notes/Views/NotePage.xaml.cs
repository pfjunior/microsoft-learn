using Notes.Models;

namespace Notes.Views;

[QueryProperty(nameof(ItemId), nameof(ItemId))]
public partial class NotePage : ContentPage
{
    public string ItemId { set { LoadNote(value); } }

    public NotePage()
	{
		InitializeComponent();

		string appDataPath = FileSystem.AppDataDirectory;
		string randomFileName = $"{Path.GetRandomFileName()}.notes.txt";

		LoadNote(Path.Combine(appDataPath, randomFileName));
	}

	#region Methods
	private void LoadNote(string fileName)
	{
		Note noteModel = new Note();
		noteModel.FileName = fileName;

		if(File.Exists(fileName))
		{
			noteModel.Date = File.GetCreationTime(fileName);
			noteModel.Text = File.ReadAllText(fileName);
		}

		BindingContext = noteModel;
	}

	#endregion

	#region Events
	private async void SaveButton_Clicked(object sender, EventArgs e)
	{
		if(BindingContext is Note note)
			File.WriteAllText(note.FileName, TextEditor.Text);

		await Shell.Current.GoToAsync("..");
	}

	private async void DeleteButton_Clicked(object sender, EventArgs e)
	{
		if (BindingContext is Note note)
		{
			if (File.Exists(note.FileName))
				File.Delete(note.FileName);
		}

		await Shell.Current.GoToAsync("..");
	} 
	#endregion
}