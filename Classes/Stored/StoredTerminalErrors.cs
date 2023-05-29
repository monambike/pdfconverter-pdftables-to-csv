using System;

// OuroWebPDFConverter
// Solução de Teste do Script - Custom Software
namespace pdfconverter_desktop
{
    // ARMAZENAMENTO DE ERROS
    // -------------------------------------------------------------
    // Descrição:
    // Classe responsável pelo armazenamento de erros em  uma  lista
    // para maior facilidade de manipulação.
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    public class StoredErrors : IEquatable<StoredErrors>
    {
        public int errorID { get; set; }
        public string errorDescription { get; set; }
        public string errorException { get; set; }

        public override string ToString()
        {
            // Retorna os dados da classe como String
            return
                "Description: " + errorDescription + " " +
                "Exception: " + errorException;
        }

        // Pega o ID do dado de acordo com o parâmetro passado
        public override int GetHashCode() { return errorID; }

        // Faz a comparação dos dados da classe com o parâmetro passado
        public override bool Equals(object obj)
        {
            if (obj == null) return false;
            StoredErrors objAsError = obj as StoredErrors;
            if (objAsError == null) return false;
            else return Equals(objAsError);
        }
        public bool Equals(StoredErrors other)
        {
            if (other == null) return false;
            return (this.errorID.Equals(other.errorID));
        }
    }
    // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    // -------------------------------------------------------------
}
